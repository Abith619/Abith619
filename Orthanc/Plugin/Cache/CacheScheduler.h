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


#pragma once

#include "CacheManager.h"
#include "ICacheFactory.h"
#include "IPrefetchPolicy.h"

#include <Compatibility.h>  // For std::unique_ptr<>
#include <MultiThreading/SharedMessageQueue.h>

#include <boost/thread.hpp>
#include <stdio.h>

namespace OrthancPlugins
{
  class CacheScheduler : public boost::noncopyable
  {
  private:
    class Prefetcher;
    class PrefetchQueue;
    class BundleScheduler;

    typedef std::map<int, BundleScheduler*>  BundleSchedulers;

    size_t                            maxPrefetchSize_;
    boost::mutex                      cacheMutex_;
    boost::mutex                      factoryMutex_;
    boost::recursive_mutex            policyMutex_;
    CacheManager&                     cache_;
    std::unique_ptr<IPrefetchPolicy>  policy_;
    BundleSchedulers                  bundles_;

    void ApplyPrefetchPolicy(int bundle,
                             const std::string& item,
                             const std::string& content);

    BundleScheduler&  GetBundleScheduler(unsigned int bundleIndex);

  public:
    CacheScheduler(CacheManager& cache,
                   unsigned int maxPrefetchSize);

    ~CacheScheduler();

    void Register(int bundle,
                  ICacheFactory* factory /* takes ownership */,
                  size_t  numThreads);

    void SetQuota(int bundle,
                  uint32_t maxCount,
                  uint64_t maxSpace);

    void RegisterPolicy(IPrefetchPolicy* policy /* takes ownership */);

    void Invalidate(int bundle,
                    const std::string& item);

    bool Access(std::string& content,
                int bundle,
                const std::string& item);

    void Prefetch(int bundle,
                  const std::string& item);

    ICacheFactory& GetFactory(int bundle);

    void SetProperty(CacheProperty property,
                     const std::string& value);

    bool LookupProperty(std::string& target,
                        CacheProperty property);

    void Clear();
  };
}
