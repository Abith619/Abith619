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


#include "ViewerToolbox.h"

#include <Logging.h>
#include <OrthancException.h>
#include <Toolbox.h>

// To gain access to ORTHANC_PLUGINS_VERSION_IS_ABOVE if Orthanc SDK <= 1.3.0
#include "../Resources/Orthanc/Plugins/OrthancPluginCppWrapper.h"

#include <json/reader.h>
#include <stdexcept>
#include <boost/lexical_cast.hpp>
#include <sys/stat.h>

namespace OrthancPlugins
{
  bool GetStringFromOrthanc(std::string& content,
                            OrthancPluginContext* context,
                            const std::string& uri)
  {
    OrthancPluginMemoryBuffer answer;

    if (OrthancPluginRestApiGet(context, &answer, uri.c_str()))
    {
      return false;
    }

    if (answer.size)
    {
      try
      {
        content.assign(reinterpret_cast<const char*>(answer.data), answer.size);
      }
      catch (std::bad_alloc&)
      {
        OrthancPluginFreeMemoryBuffer(context, &answer);
        throw Orthanc::OrthancException(Orthanc::ErrorCode_NotEnoughMemory);
      }
    }

    OrthancPluginFreeMemoryBuffer(context, &answer);
    return true;
  }


  bool GetJsonFromOrthanc(Json::Value& json,
                          OrthancPluginContext* context,
                          const std::string& uri)
  {
    OrthancPluginMemoryBuffer answer;

    if (OrthancPluginRestApiGet(context, &answer, uri.c_str()))
    {
      return false;
    }

    if (answer.size)
    {
      try
      {
        const char* data = reinterpret_cast<const char*>(answer.data);
        Json::Reader reader;
        if (!reader.parse(data, data + answer.size, json, 
                          false /* don't collect comments */))
        {
          return false;
        }
      }
      catch (std::runtime_error&)
      {
        OrthancPluginFreeMemoryBuffer(context, &answer);
        return false;
      }
    }

    OrthancPluginFreeMemoryBuffer(context, &answer);
    return true;
  }




  bool TokenizeVector(std::vector<float>& result,
                      const std::string& value,
                      unsigned int expectedSize)
  {
    std::vector<std::string> tokens;
    Orthanc::Toolbox::TokenizeString(tokens, value, '\\');

    if (tokens.size() != expectedSize)
    {
      return false;
    }

    result.resize(tokens.size());

    for (size_t i = 0; i < tokens.size(); i++)
    {
      try
      {
        result[i] = boost::lexical_cast<float>(tokens[i]);
      }
      catch (boost::bad_lexical_cast&)
      {
        return false;
      }
    }

    return true;
  }


  void CompressUsingDeflate(std::string& compressed,
                            OrthancPluginContext* context,
                            const void* uncompressed,
                            size_t uncompressedSize)
  {
    OrthancPluginMemoryBuffer tmp;
   
    OrthancPluginErrorCode code = OrthancPluginBufferCompression(
      context, &tmp, uncompressed, uncompressedSize, 
      OrthancPluginCompressionType_Zlib, 0 /*compress*/);
      
    if (code != OrthancPluginErrorCode_Success)
    {
      throw Orthanc::OrthancException(static_cast<Orthanc::ErrorCode>(code));
    }

    try
    {
      compressed.assign(reinterpret_cast<const char*>(tmp.data), tmp.size);
    }
    catch (...)
    {
      throw Orthanc::OrthancException(Orthanc::ErrorCode_NotEnoughMemory);
    }

    OrthancPluginFreeMemoryBuffer(context, &tmp);
  }


  const char* GetMimeType(const std::string& path)
  {
    size_t dot = path.find_last_of('.');

    std::string extension = (dot == std::string::npos) ? "" : path.substr(dot);
    std::transform(extension.begin(), extension.end(), extension.begin(), tolower);

    if (extension == ".html")
    {
      return "text/html";
    }
    else if (extension == ".css")
    {
      return "text/css";
    }
    else if (extension == ".js")
    {
      return "application/javascript";
    }
    else if (extension == ".gif")
    {
      return "image/gif";
    }
    else if (extension == ".svg")
    {
      return "image/svg+xml";
    }
    else if (extension == ".json")
    {
      return "application/json";
    }
    else if (extension == ".xml")
    {
      return "application/xml";
    }
    else if (extension == ".png")
    {
      return "image/png";
    }
    else if (extension == ".jpg" || extension == ".jpeg")
    {
      return "image/jpeg";
    }
    else
    {
      return "application/octet-stream";
    }
  }


  bool ReadConfiguration(Json::Value& configuration,
                         OrthancPluginContext* context)
  {
    std::string s;

    {
      char* tmp = OrthancPluginGetConfiguration(context);
      if (tmp == NULL)
      {
        LOG(ERROR) << "Error while retrieving the configuration from Orthanc";
        return false;
      }

      s.assign(tmp);
      OrthancPluginFreeString(context, tmp);      
    }

    Json::Reader reader;
    if (reader.parse(s, configuration))
    {
      return true;
    }
    else
    {
      LOG(ERROR) << "Unable to parse the configuration";
      return false;
    }
  }


  std::string GetStringValue(const Json::Value& configuration,
                             const std::string& key,
                             const std::string& defaultValue)
  {
    if (configuration.type() != Json::objectValue ||
        !configuration.isMember(key) ||
        configuration[key].type() != Json::stringValue)
    {
      return defaultValue;
    }
    else
    {
      return configuration[key].asString();
    }
  }  


  int GetIntegerValue(const Json::Value& configuration,
                      const std::string& key,
                      int defaultValue)
  {
    if (configuration.type() != Json::objectValue ||
        !configuration.isMember(key) ||
        configuration[key].type() != Json::intValue)
    {
      return defaultValue;
    }
    else
    {
      return configuration[key].asInt();
    }
  }


  OrthancPluginPixelFormat Convert(Orthanc::PixelFormat format)
  {
    switch (format)
    {
      case Orthanc::PixelFormat_Grayscale16:
        return OrthancPluginPixelFormat_Grayscale16;

      case Orthanc::PixelFormat_Grayscale8:
        return OrthancPluginPixelFormat_Grayscale8;

      case Orthanc::PixelFormat_RGB24:
        return OrthancPluginPixelFormat_RGB24;

#if ORTHANC_PLUGINS_VERSION_IS_ABOVE(1, 3, 1)
      case Orthanc::PixelFormat_RGB48:
        return OrthancPluginPixelFormat_RGB48;
#endif

      case Orthanc::PixelFormat_RGBA32:
        return OrthancPluginPixelFormat_RGBA32;

      case Orthanc::PixelFormat_SignedGrayscale16:
        return OrthancPluginPixelFormat_SignedGrayscale16;

      default:
        throw Orthanc::OrthancException(Orthanc::ErrorCode_ParameterOutOfRange);
    }
  }


  Orthanc::PixelFormat Convert(OrthancPluginPixelFormat format)
  {
    switch (format)
    {
      case OrthancPluginPixelFormat_Grayscale16:
        return Orthanc::PixelFormat_Grayscale16;

      case OrthancPluginPixelFormat_Grayscale8:
        return Orthanc::PixelFormat_Grayscale8;

      case OrthancPluginPixelFormat_RGB24:
        return Orthanc::PixelFormat_RGB24;

#if ORTHANC_PLUGINS_VERSION_IS_ABOVE(1, 3, 1)
      case OrthancPluginPixelFormat_RGB48:
        return Orthanc::PixelFormat_RGB48;
#endif

      case OrthancPluginPixelFormat_RGBA32:
        return Orthanc::PixelFormat_RGBA32;

      case OrthancPluginPixelFormat_SignedGrayscale16:
        return Orthanc::PixelFormat_SignedGrayscale16;

      default:
        throw Orthanc::OrthancException(Orthanc::ErrorCode_ParameterOutOfRange);
    }
  }


  void WriteJpegToMemory(std::string& result,
                         OrthancPluginContext* context,
                         const Orthanc::ImageAccessor& accessor,
                         uint8_t quality)
  {
    OrthancPluginMemoryBuffer tmp;
   
    OrthancPluginErrorCode code = OrthancPluginCompressJpegImage
      (context, &tmp, Convert(accessor.GetFormat()), 
       accessor.GetWidth(), accessor.GetHeight(), accessor.GetPitch(),
       accessor.GetConstBuffer(), quality);

    if (code != OrthancPluginErrorCode_Success)
    {
      throw Orthanc::OrthancException(static_cast<Orthanc::ErrorCode>(code));
    }

    try
    {
      result.assign(reinterpret_cast<const char*>(tmp.data), tmp.size);
    }
    catch (...)
    {
      throw Orthanc::OrthancException(Orthanc::ErrorCode_NotEnoughMemory);
    }

    OrthancPluginFreeMemoryBuffer(context, &tmp);
  }



  ImageReader::ImageReader(OrthancPluginContext* context,
                           const std::string& image,
                           OrthancPluginImageFormat format) : context_(context)
  {
    image_ = OrthancPluginUncompressImage(context_, image.c_str(), image.size(), format);

    if (image_ == NULL)
    {
      throw Orthanc::OrthancException(Orthanc::ErrorCode_CorruptedFile);
    }
  }


  ImageReader::~ImageReader()
  {
    OrthancPluginFreeImage(context_, image_);
  }


  void ImageReader::GetAccessor(Orthanc::ImageAccessor& target) const
  {
    target.AssignReadOnly(Convert(OrthancPluginGetImagePixelFormat(context_, image_)),
                          OrthancPluginGetImageWidth(context_, image_),
                          OrthancPluginGetImageHeight(context_, image_),
                          OrthancPluginGetImagePitch(context_, image_),
                          OrthancPluginGetImageBuffer(context_, image_));
  }
}
