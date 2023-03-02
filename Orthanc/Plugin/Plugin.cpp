/**
 * Orthanc - A Lightweight, RESTful DICOM Store
 * Copyright (C) 2012-2016 Sebastien Jodogne, Medical Physics
 * Department, University Hospital of Liege, Belgium
 * Copyright (C) 2017-2020 Osimis S.A., Belgium
 *
 * This program is free software: you can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public License
 * as published by the Free Software Foundation, either version 3 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Affero General Public License for more details.
 * 
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 **/


#include "../Resources/Orthanc/Plugins/OrthancPluginCppWrapper.h"
#include "ViewerToolbox.h"
#include "ViewerPrefetchPolicy.h"
#include "DecodedImageAdapter.h"
#include "SeriesInformationAdapter.h"

#include <DicomFormat/DicomMap.h>
#include <Logging.h>
#include <OrthancException.h>
#include <SystemToolbox.h>
#include <Toolbox.h>

#include <boost/thread.hpp>
#include <boost/lexical_cast.hpp>
#include <EmbeddedResources.h>
#include <boost/filesystem.hpp>


/**
 * We force the redefinition of the "ORTHANC_PLUGINS_API" macro, that
 * was left empty with gcc until Orthanc SDK 1.5.7 (no "default"
 * visibility). This causes the version script, if run from "Holy
 * Build Box", to make private the 4 global functions of the plugin.
 **/

#undef ORTHANC_PLUGINS_API

#ifdef WIN32
#  define ORTHANC_PLUGINS_API __declspec(dllexport)
#elif __GNUC__ >= 4
#  define ORTHANC_PLUGINS_API __attribute__ ((visibility ("default")))
#else
#  define ORTHANC_PLUGINS_API
#endif



class CacheContext
{
private:
  class DynamicString : public Orthanc::IDynamicObject
  {
  private:
    std::string  value_;

  public:
    explicit DynamicString(const char* value) : value_(value)
    {
    }
    
    const std::string& GetValue() const
    {
      return value_;
    }
  };

  Orthanc::FilesystemStorage  storage_;
  Orthanc::SQLite::Connection  db_;

  std::unique_ptr<OrthancPlugins::CacheManager>  cache_;
  std::unique_ptr<OrthancPlugins::CacheScheduler>  scheduler_;

  Orthanc::SharedMessageQueue  newInstances_;
  bool stop_;
  boost::thread newInstancesThread_;

  static void NewInstancesThread(CacheContext* cache)
  {
    while (!cache->stop_)
    {
      std::unique_ptr<Orthanc::IDynamicObject> obj(cache->newInstances_.Dequeue(100));
      if (obj.get() != NULL)
      {
        const std::string& instanceId = dynamic_cast<DynamicString&>(*obj).GetValue();

        // On the reception of a new instance, indalidate the parent series of the instance
        std::string uri = "/instances/" + std::string(instanceId);
        Json::Value instance;
        if (OrthancPlugins::GetJsonFromOrthanc(instance, OrthancPlugins::GetGlobalContext(), uri))
        {
          std::string seriesId = instance["ParentSeries"].asString();
          cache->GetScheduler().Invalidate(OrthancPlugins::CacheBundle_SeriesInformation, seriesId);
        }
      }
    }
  }


public:
  explicit CacheContext(const std::string& path) : storage_(path), stop_(false)
  {
    boost::filesystem::path p(path);
    db_.Open((p / "cache.db").string());

    cache_.reset(new OrthancPlugins::CacheManager(OrthancPlugins::GetGlobalContext(), db_, storage_));
    //cache_->SetSanityCheckEnabled(true);  // For debug

    scheduler_.reset(new OrthancPlugins::CacheScheduler(*cache_, 100));

    newInstancesThread_ = boost::thread(NewInstancesThread, this);
  }

  ~CacheContext()
  {
    stop_ = true;
    if (newInstancesThread_.joinable())
    {
      newInstancesThread_.join();
    }

    scheduler_.reset(NULL);
    cache_.reset(NULL);
  }

  OrthancPlugins::CacheScheduler& GetScheduler()
  {
    return *scheduler_;
  }

  void SignalNewInstance(const char* instanceId)
  {
    newInstances_.Enqueue(new DynamicString(instanceId));
  }
};



static CacheContext* cache_ = NULL;



static OrthancPluginErrorCode OnChangeCallback(OrthancPluginChangeType changeType,
                                               OrthancPluginResourceType resourceType,
                                               const char* resourceId)
{
  try
  {
    if (changeType == OrthancPluginChangeType_NewInstance &&
        resourceType == OrthancPluginResourceType_Instance)
    {
      cache_->SignalNewInstance(resourceId);
    }

    return OrthancPluginErrorCode_Success;
  }
  catch (std::runtime_error& e)
  {
    LOG(ERROR) << e.what();
    return OrthancPluginErrorCode_Success;  // Ignore error
  }
}



template <enum OrthancPlugins::CacheBundle bundle>
static OrthancPluginErrorCode ServeCache(OrthancPluginRestOutput* output,
                                         const char* url,
                                         const OrthancPluginHttpRequest* request)
{
  try
  {
    if (request->method != OrthancPluginHttpMethod_Get)
    {
      OrthancPluginSendMethodNotAllowed(OrthancPlugins::GetGlobalContext(), output, "GET");
      return OrthancPluginErrorCode_Success;
    }

    const std::string id = request->groups[0];
    std::string content;

    if (cache_->GetScheduler().Access(content, bundle, id))
    {
      OrthancPluginAnswerBuffer(OrthancPlugins::GetGlobalContext(), output, content.c_str(), content.size(), "application/json");
    }
    else
    {
      OrthancPluginSendHttpStatusCode(OrthancPlugins::GetGlobalContext(), output, 404);
    }

    return OrthancPluginErrorCode_Success;
  }
  catch (Orthanc::OrthancException& e)
  {
    LOG(ERROR) << e.What();
    return OrthancPluginErrorCode_Plugin;
  }
  catch (std::runtime_error& e)
  {
    LOG(ERROR) << e.what();
    return OrthancPluginErrorCode_Plugin;
  }
  catch (boost::bad_lexical_cast&)
  {
    LOG(ERROR) << "Bad lexical cast";
    return OrthancPluginErrorCode_Plugin;
  }
}




#if ORTHANC_STANDALONE == 0
static OrthancPluginErrorCode ServeWebViewer(OrthancPluginRestOutput* output,
                                             const char* url,
                                             const OrthancPluginHttpRequest* request)
{
  if (request->method != OrthancPluginHttpMethod_Get)
  {
    OrthancPluginSendMethodNotAllowed(OrthancPlugins::GetGlobalContext(), output, "GET");
    return OrthancPluginErrorCode_Success;
  }

  const std::string path = std::string(WEB_VIEWER_PATH) + std::string(request->groups[0]);
  const char* mime = OrthancPlugins::GetMimeType(path);

  std::string s;
  try
  {
    Orthanc::SystemToolbox::ReadFile(s, path);
    const char* resource = s.size() ? s.c_str() : NULL;
    OrthancPluginAnswerBuffer(OrthancPlugins::GetGlobalContext(), output, resource, s.size(), mime);
  }
  catch (Orthanc::OrthancException&)
  {
    LOG(ERROR) << "Inexistent file in served folder: " << path;
    OrthancPluginSendHttpStatusCode(OrthancPlugins::GetGlobalContext(), output, 404);
  }

  return OrthancPluginErrorCode_Success;
}
#endif



template <enum Orthanc::EmbeddedResources::DirectoryResourceId folder>
static OrthancPluginErrorCode ServeEmbeddedFolder(OrthancPluginRestOutput* output,
                                                  const char* url,
                                                  const OrthancPluginHttpRequest* request)
{
  if (request->method != OrthancPluginHttpMethod_Get)
  {
    OrthancPluginSendMethodNotAllowed(OrthancPlugins::GetGlobalContext(), output, "GET");
    return OrthancPluginErrorCode_Success;
  }

  std::string path = "/" + std::string(request->groups[0]);
  const char* mime = OrthancPlugins::GetMimeType(path);

  try
  {
    std::string s;
    Orthanc::EmbeddedResources::GetDirectoryResource(s, folder, path.c_str());

    const char* resource = s.size() ? s.c_str() : NULL;
    OrthancPluginAnswerBuffer(OrthancPlugins::GetGlobalContext(), output, resource, s.size(), mime);

    return OrthancPluginErrorCode_Success;
  }
  catch (std::runtime_error&)
  {
    LOG(ERROR) << "Unknown static resource in plugin: " << request->groups[0];
    OrthancPluginSendHttpStatusCode(OrthancPlugins::GetGlobalContext(), output, 404);
    return OrthancPluginErrorCode_Success;
  }
}



static OrthancPluginErrorCode IsStableSeries(OrthancPluginRestOutput* output,
                                             const char* url,
                                             const OrthancPluginHttpRequest* request)
{
  try
  {
    if (request->method != OrthancPluginHttpMethod_Get)
    {
      OrthancPluginSendMethodNotAllowed(OrthancPlugins::GetGlobalContext(), output, "GET");
      return OrthancPluginErrorCode_Success;
    }

    const std::string id = request->groups[0];
    Json::Value series;

    if (OrthancPlugins::GetJsonFromOrthanc(series, OrthancPlugins::GetGlobalContext(), "/series/" + id) &&
        series.type() == Json::objectValue)
    {
      bool value = (series["IsStable"].asBool() ||
                    series["Status"].asString() == "Complete");
      std::string answer = value ? "true" : "false";
      OrthancPluginAnswerBuffer(OrthancPlugins::GetGlobalContext(), output, answer.c_str(), answer.size(), "application/json");
    }
    else
    {
      OrthancPluginSendHttpStatusCode(OrthancPlugins::GetGlobalContext(), output, 404);
    }

    return OrthancPluginErrorCode_Success;
  }
  catch (Orthanc::OrthancException& e)
  {
    LOG(ERROR) << e.What();
    return OrthancPluginErrorCode_Plugin;
  }
  catch (std::runtime_error& e)
  {
    LOG(ERROR) << e.what();
    return OrthancPluginErrorCode_Plugin;
  }
  catch (boost::bad_lexical_cast&)
  {
    LOG(ERROR) << "Bad lexical cast";
    return OrthancPluginErrorCode_Plugin;
  }
}



void ParseConfiguration(int& decodingThreads,
                        boost::filesystem::path& cachePath,
                        int& cacheSize)
{
  /* Read the configuration of the Web viewer */
  Json::Value configuration;
  if (!OrthancPlugins::ReadConfiguration(configuration, OrthancPlugins::GetGlobalContext()))
  {
    throw Orthanc::OrthancException(Orthanc::ErrorCode_BadFileFormat);    
  }

  // By default, the cache of the Web viewer is located inside the
  // "StorageDirectory" of Orthanc
  cachePath = OrthancPlugins::GetStringValue(configuration, "StorageDirectory", ".");
  cachePath /= "WebViewerCache";

  static const char* CONFIG_WEB_VIEWER = "WebViewer";
  if (configuration.isMember(CONFIG_WEB_VIEWER))
  {

    std::string key = "CachePath";
    if (!configuration[CONFIG_WEB_VIEWER].isMember(key))
    {
      // For backward compatibility with the initial release of the Web viewer
      key = "Cache";
    }

    cachePath = OrthancPlugins::GetStringValue(configuration[CONFIG_WEB_VIEWER], key, cachePath.string());
    cacheSize = OrthancPlugins::GetIntegerValue(configuration[CONFIG_WEB_VIEWER], "CacheSize", cacheSize);
    decodingThreads = OrthancPlugins::GetIntegerValue(configuration[CONFIG_WEB_VIEWER], "Threads", decodingThreads);
  }

  if (decodingThreads <= 0 ||
      cacheSize <= 0)
  {
    throw Orthanc::OrthancException(Orthanc::ErrorCode_ParameterOutOfRange);
  }

}


static bool DisplayPerformanceWarning()
{
  (void) DisplayPerformanceWarning;   // Disable warning about unused function
  LOG(WARNING) << "Performance warning in Web viewer: "
               << "Non-release build, runtime debug assertions are turned on";
  return true;
}


extern "C"
{
  ORTHANC_PLUGINS_API int32_t OrthancPluginInitialize(OrthancPluginContext* context)
  {
    using namespace OrthancPlugins;

    OrthancPlugins::SetGlobalContext(context);

#if ORTHANC_FRAMEWORK_VERSION_IS_ABOVE(1, 7, 2)
    Orthanc::Logging::InitializePluginContext(context);
#else
    Orthanc::Logging::Initialize(context);
#endif

    assert(DisplayPerformanceWarning());
    LOG(WARNING) << "Initializing the Web viewer";


    /* Check the version of the Orthanc core */
    if (OrthancPluginCheckVersion(context) == 0)
    {
      char info[1024];
      sprintf(info, "Your version of Orthanc (%s) must be above %d.%d.%d to run this plugin",
              context->orthancVersion,
              ORTHANC_PLUGINS_MINIMAL_MAJOR_NUMBER,
              ORTHANC_PLUGINS_MINIMAL_MINOR_NUMBER,
              ORTHANC_PLUGINS_MINIMAL_REVISION_NUMBER);
      OrthancPluginLogError(context, info);
      return -1;
    }

    OrthancPluginSetDescription(context, "Provides a Web viewer of DICOM series within Orthanc.");


    /* By default, use half of the available processing cores for the decoding of DICOM images */
    int decodingThreads = boost::thread::hardware_concurrency() / 2;
    if (decodingThreads == 0)
    {
      decodingThreads = 1;
    }

    try
    {
      /* By default, a cache of 100 MB is used */
      int cacheSize = 100; 

      boost::filesystem::path cachePath;
      ParseConfiguration(decodingThreads, cachePath, cacheSize);

      LOG(WARNING) << "Web viewer using " << decodingThreads
                   << " threads for the decoding of the DICOM images";

      LOG(WARNING) << "Storing the cache of the Web viewer in folder: " << cachePath.string();

   
      /* Create the cache */
      cache_ = new CacheContext(cachePath.string());
      CacheScheduler& scheduler = cache_->GetScheduler();


      /* Look for a change in the versions */
      std::string orthancVersion("unknown"), webViewerVersion("unknown");
      bool clear = false;
      if (!scheduler.LookupProperty(orthancVersion, CacheProperty_OrthancVersion) ||
          orthancVersion != std::string(context->orthancVersion))
      {
        LOG(WARNING) << "The version of Orthanc has changed from \"" << orthancVersion
                     << "\" to \"" << context->orthancVersion
                     << "\": The cache of the Web viewer will be cleared";
        clear = true;
      }

      if (!scheduler.LookupProperty(webViewerVersion, CacheProperty_WebViewerVersion) ||
          webViewerVersion != std::string(ORTHANC_PLUGIN_VERSION))
      {
        LOG(WARNING) << "The version of the Web viewer plugin has changed from \""
                     << webViewerVersion << "\" to \"" << ORTHANC_PLUGIN_VERSION
                     << "\": The cache of the Web viewer will be cleared";
        clear = true;
      }


      /* Clear the cache if needed */
      if (clear)
      {
        LOG(WARNING) << "Clearing the cache of the Web viewer";
        scheduler.Clear();
        scheduler.SetProperty(CacheProperty_OrthancVersion, context->orthancVersion);
        scheduler.SetProperty(CacheProperty_WebViewerVersion, ORTHANC_PLUGIN_VERSION);
      }
      else
      {
        LOG(INFO) << "No change in the versions, no need to clear the cache of the Web viewer";
      }


      /* Configure the cache */
      scheduler.RegisterPolicy(new ViewerPrefetchPolicy(context));
      scheduler.Register(CacheBundle_SeriesInformation, 
                         new SeriesInformationAdapter(context, scheduler), 1);
      scheduler.Register(CacheBundle_DecodedImage, 
                         new DecodedImageAdapter(context), decodingThreads);


      /* Set the quotas */
      scheduler.SetQuota(CacheBundle_SeriesInformation, 1000, 0);    // Keep info about 1000 series
      
      LOG(WARNING) << "Web viewer using a cache of " << cacheSize << " MB";

      scheduler.SetQuota(CacheBundle_DecodedImage, 0, static_cast<uint64_t>(cacheSize) * 1024 * 1024);
    }
    catch (std::runtime_error& e)
    {
      LOG(ERROR) << e.what();
      return -1;
    }
    catch (Orthanc::OrthancException& e)
    {
      if (e.GetErrorCode() == Orthanc::ErrorCode_BadFileFormat)
      {
        LOG(ERROR) << "Unable to read the configuration of the Web viewer plugin";
      }
      else
      {
        LOG(ERROR) << e.What();
      }
      return -1;
    }


    /* Install the callbacks */
    OrthancPluginRegisterRestCallbackNoLock(context, "/web-viewer/series/(.*)", ServeCache<CacheBundle_SeriesInformation>);
    OrthancPluginRegisterRestCallbackNoLock(context, "/web-viewer/is-stable-series/(.*)", IsStableSeries);
    OrthancPluginRegisterRestCallbackNoLock(context, "/web-viewer/instances/(.*)", ServeCache<CacheBundle_DecodedImage>);
    OrthancPluginRegisterRestCallbackNoLock(context, "/web-viewer/libs/(.*)", ServeEmbeddedFolder<Orthanc::EmbeddedResources::JAVASCRIPT_LIBS>);

#if ORTHANC_STANDALONE == 1
    OrthancPluginRegisterRestCallbackNoLock(context, "/web-viewer/app/(.*)", ServeEmbeddedFolder<Orthanc::EmbeddedResources::WEB_VIEWER>);
#else
    OrthancPluginRegisterRestCallbackNoLock(context, "/web-viewer/app/(.*)", ServeWebViewer);
#endif

    OrthancPluginRegisterOnChangeCallback(context, OnChangeCallback);


    /* Extend the default Orthanc Explorer with custom JavaScript */
    std::string explorer;
    Orthanc::EmbeddedResources::GetFileResource(explorer, Orthanc::EmbeddedResources::ORTHANC_EXPLORER);
    OrthancPluginExtendOrthancExplorer(context, explorer.c_str());

    return 0;
  }


  ORTHANC_PLUGINS_API void OrthancPluginFinalize()
  {
    LOG(WARNING) << "Finalizing the Web viewer";

    if (cache_ != NULL)
    {
      delete cache_;
      cache_ = NULL;
    }

    Orthanc::Logging::Finalize();
  }


  ORTHANC_PLUGINS_API const char* OrthancPluginGetName()
  {
    return "web-viewer";
  }


  ORTHANC_PLUGINS_API const char* OrthancPluginGetVersion()
  {
    return ORTHANC_PLUGIN_VERSION;
  }
}
