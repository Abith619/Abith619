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


#include "CacheScheduler.h"

#include "CacheIndex.h"

#include <Compatibility.h>
#include <OrthancException.h>
#include <stdio.h>

namespace OrthancPlugins
{
  class DynamicString : public Orthanc::IDynamicObject
  {
  private:
    std::string   value_;

  public:
    explicit DynamicString(const std::string& value) : value_(value)
    {
    }

    const std::string& GetValue() const
    {
      return value_;
    }
  };


  class CacheScheduler::PrefetchQueue : public boost::noncopyable
  {
  private:
    boost::mutex                 mutex_;
    Orthanc::SharedMessageQueue  queue_;
    std::set<std::string>        content_;

  public:
    explicit PrefetchQueue(size_t maxSize) : queue_(maxSize)
    {
      queue_.SetLifoPolicy();
    }

    void Enqueue(const std::string& item)
    {
      boost::mutex::scoped_lock lock(mutex_);

      if (content_.find(item) != content_.end())
      {
        // This cache index is already pending in the queue
        return;
      }

      content_.insert(item);
      queue_.Enqueue(new DynamicString(item));
    }

    DynamicString* Dequeue(int32_t msTimeout)
    {
      std::unique_ptr<Orthanc::IDynamicObject> message(queue_.Dequeue(msTimeout));
      if (message.get() == NULL)
      {
        return NULL;
      }

      const DynamicString& index = dynamic_cast<const DynamicString&>(*message);

      {
        boost::mutex::scoped_lock lock(mutex_);
        content_.erase(index.GetValue());
      }

      return dynamic_cast<DynamicString*>(message.release());
    }
  };


  class CacheScheduler::Prefetcher : public boost::noncopyable
  {
  private:
    int             bundleIndex_;
    ICacheFactory&  factory_;
    CacheManager&   cache_;
    boost::mutex&   cacheMutex_;
    PrefetchQueue&  queue_;

    bool            done_;
    boost::thread   thread_;
    boost::mutex    invalidatedMutex_;
    bool            invalidated_;
    std::string     prefetching_;

    static void Worker(Prefetcher* that)
    {
      while (!(that->done_))
      {
        std::unique_ptr<DynamicString> prefetch(that->queue_.Dequeue(500));

        try
        {
          if (prefetch.get() != NULL)
          {
            {
              boost::mutex::scoped_lock lock(that->invalidatedMutex_);
              that->invalidated_ = false;
              that->prefetching_ = prefetch->GetValue();
            }

            {
              boost::mutex::scoped_lock lock(that->cacheMutex_);
              if (that->cache_.IsCached(that->bundleIndex_, prefetch->GetValue()))
              {
                // This item is already cached
                continue;
              }
            }

            std::string content;

            try
            {
              if (!that->factory_.Create(content, prefetch->GetValue()))
              {
                // The factory cannot generate this item
                continue;
              }
            }
            catch (...)
            {
              // Exception
              continue;
            }

            {
              boost::mutex::scoped_lock lock(that->invalidatedMutex_);
              if (that->invalidated_)
              {
                // This item has been invalidated
                continue;
              }
              
              {
                boost::mutex::scoped_lock lock2(that->cacheMutex_);
                that->cache_.Store(that->bundleIndex_, prefetch->GetValue(), content);
              }
            }
          }
        }
        catch (std::bad_alloc&)
        {
          OrthancPluginLogError(that->cache_.GetPluginContext(), 
                                "Not enough memory for the prefetcher of the Web viewer to work");
        }
        catch (...)
        {
          OrthancPluginLogError(that->cache_.GetPluginContext(), 
                                "Unhandled native exception inside the prefetcher of the Web viewer");
        }
      }
    }


  public:
    Prefetcher(int             bundleIndex,
               ICacheFactory&  factory,
               CacheManager&   cache,
               boost::mutex&   cacheMutex,
               PrefetchQueue&  queue) :
      bundleIndex_(bundleIndex),
      factory_(factory),
      cache_(cache),
      cacheMutex_(cacheMutex),
      queue_(queue)
    {
      done_ = false;
      thread_ = boost::thread(Worker, this);
    }

    ~Prefetcher()
    {
      done_ = true;
      if (thread_.joinable())
      {
        thread_.join();
      }
    }

    void SignalInvalidated(const std::string& item)
    {
      boost::mutex::scoped_lock lock(invalidatedMutex_);

      if (prefetching_ == item)
      {
        invalidated_ = true;
      }
    }
  };



  class CacheScheduler::BundleScheduler
  {
  private:
    std::unique_ptr<ICacheFactory>   factory_;
    PrefetchQueue                    queue_;
    std::vector<Prefetcher*>         prefetchers_;

  public:
    BundleScheduler(int bundleIndex,
                    ICacheFactory* factory,
                    CacheManager&   cache,
                    boost::mutex&   cacheMutex,
                    size_t numThreads,
                    size_t queueSize) :
      factory_(factory),
      queue_(queueSize)
    {
      prefetchers_.resize(numThreads, NULL);

      for (size_t i = 0; i < numThreads; i++)
      {
        prefetchers_[i] = new Prefetcher(bundleIndex, *factory_, cache, cacheMutex, queue_);
      }
    }

    ~BundleScheduler()
    {
      for (size_t i = 0; i < prefetchers_.size(); i++)
      {
        if (prefetchers_[i] != NULL)
          delete prefetchers_[i];
      }
    }

    void Invalidate(const std::string& item)
    {
      for (size_t i = 0; i < prefetchers_.size(); i++)
      {
        prefetchers_[i]->SignalInvalidated(item);
      }
    }

    void Prefetch(const std::string& item)
    {
      queue_.Enqueue(item);
    }

    bool CallFactory(std::string& content,
                     const std::string& item)
    {
      content.clear();
      return factory_->Create(content, item);
    }

    ICacheFactory& GetFactory()
    {
      return *factory_;
    }
  };



  CacheScheduler::BundleScheduler&  CacheScheduler::GetBundleScheduler(unsigned int bundleIndex)
  {
    boost::mutex::scoped_lock lock(factoryMutex_);

    BundleSchedulers::iterator it = bundles_.find(bundleIndex);
    if (it == bundles_.end())
    {
      // No factory associated with this bundle
      throw Orthanc::OrthancException(Orthanc::ErrorCode_ParameterOutOfRange);
    }

    return *(it->second);
  }


  
  CacheScheduler::CacheScheduler(CacheManager& cache,
                                 unsigned int maxPrefetchSize) :
    maxPrefetchSize_(maxPrefetchSize),
    cache_(cache)
  {
  }


  CacheScheduler::~CacheScheduler()
  {
    for (BundleSchedulers::iterator it = bundles_.begin(); 
         it != bundles_.end(); ++it)
    {
      delete it->second;
    }
  }


  void CacheScheduler::Register(int bundle, 
                                ICacheFactory* factory /* takes ownership */,
                                size_t  numThreads)
  {
    boost::mutex::scoped_lock lock(factoryMutex_);

    BundleSchedulers::iterator it = bundles_.find(bundle);
    if (it != bundles_.end())
    {
      // This bundle is already registered
      throw Orthanc::OrthancException(Orthanc::ErrorCode_BadSequenceOfCalls);
    }

    bundles_[bundle] = new BundleScheduler(bundle, factory, cache_, cacheMutex_, numThreads, maxPrefetchSize_);
  }


  void CacheScheduler::SetQuota(int bundle,
                                uint32_t maxCount,
                                uint64_t maxSpace)
  {
    boost::mutex::scoped_lock lock(cacheMutex_);
    cache_.SetBundleQuota(bundle, maxCount, maxSpace);
  }


  void CacheScheduler::Invalidate(int bundle,
                                  const std::string& item)
  {
    {
      boost::mutex::scoped_lock lock(cacheMutex_);
      cache_.Invalidate(bundle, item);
    }

    GetBundleScheduler(bundle).Invalidate(item);
  }


  void CacheScheduler::ApplyPrefetchPolicy(int bundle,
                                           const std::string& item,
                                           const std::string& content)
  {
    boost::recursive_mutex::scoped_lock lock(policyMutex_);

    if (policy_.get() != NULL)
    {
      std::list<CacheIndex> toPrefetch;

      {
        policy_->Apply(toPrefetch, *this, CacheIndex(bundle, item), content);
      }

      for (std::list<CacheIndex>::const_reverse_iterator
             it = toPrefetch.rbegin(); it != toPrefetch.rend(); ++it)
      {
        Prefetch(it->GetBundle(), it->GetItem());
      }
    }
  }


  bool CacheScheduler::Access(std::string& content,
                              int bundle,
                              const std::string& item)
  {
    bool existing;

    {
      boost::mutex::scoped_lock lock(cacheMutex_);
      existing = cache_.Access(content, bundle, item);
    }

    if (existing)
    {
      ApplyPrefetchPolicy(bundle, item, content);
      return true;
    }

    if (!GetBundleScheduler(bundle).CallFactory(content, item))
    {
      // This item cannot be generated by the factory
      return false;
    }

    {
      boost::mutex::scoped_lock lock(cacheMutex_);
      cache_.Store(bundle, item, content);
    }

    ApplyPrefetchPolicy(bundle, item, content);

    return true;
  }


  void CacheScheduler::Prefetch(int bundle,
                                const std::string& item)
  {
    GetBundleScheduler(bundle).Prefetch(item);
  }


  void CacheScheduler::RegisterPolicy(IPrefetchPolicy* policy)
  {
    boost::recursive_mutex::scoped_lock lock(policyMutex_);
    policy_.reset(policy);
  }


  ICacheFactory& CacheScheduler::GetFactory(int bundle)
  {
    return GetBundleScheduler(bundle).GetFactory();
  }


  void CacheScheduler::SetProperty(CacheProperty property,
                   const std::string& value)
  {
    boost::mutex::scoped_lock lock(cacheMutex_);
    cache_.SetProperty(property, value);
  }

  
  bool CacheScheduler::LookupProperty(std::string& target,
                                      CacheProperty property)
  {
    boost::mutex::scoped_lock lock(cacheMutex_);
    return cache_.LookupProperty(target, property);
  }


  void CacheScheduler::Clear()
  {
    boost::mutex::scoped_lock lock(cacheMutex_);
    return cache_.Clear();
  }
}
