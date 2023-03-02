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

#include <FileStorage/FilesystemStorage.h>
#include <SQLite/Connection.h>

#include <orthanc/OrthancCPlugin.h>

#include <boost/shared_ptr.hpp>

namespace OrthancPlugins
{
  enum CacheProperty
  {
    CacheProperty_OrthancVersion,
    CacheProperty_WebViewerVersion
  };


  class CacheManager : public boost::noncopyable
  {
  private:
    struct PImpl;
    boost::shared_ptr<PImpl> pimpl_;

    class Bundle;
    class BundleQuota;

    typedef std::map<int, Bundle>  Bundles;
    typedef std::map<int, BundleQuota>  BundleQuotas;

    const BundleQuota& GetBundleQuota(int bundleIndex) const;

    Bundle GetBundle(int bundleIndex) const;

    void MakeRoom(Bundle& bundle,
                  std::list<std::string>& toRemove,
                  int bundleIndex,
                  const BundleQuota& quota);

    void EnsureQuota(int bundleIndex,
                     const BundleQuota& quota);

    void ReadBundleStatistics();

    void Open();

    bool LocateInCache(std::string& uuid,
                       uint64_t& size,
                       int bundle,
                       const std::string& item);

    void SanityCheck();  // Only for debug


  public:
    CacheManager(OrthancPluginContext* context,
                 Orthanc::SQLite::Connection& db,
                 Orthanc::FilesystemStorage& storage);

    OrthancPluginContext* GetPluginContext() const;

    void SetSanityCheckEnabled(bool enabled);

    void Clear();

    void Clear(int bundle);

    void SetBundleQuota(int bundle,
                        uint32_t maxCount,
                        uint64_t maxSpace);

    void SetDefaultQuota(uint32_t maxCount,
                         uint64_t maxSpace);

    bool IsCached(int bundle,
                  const std::string& item);

    bool Access(std::string& content,
                int bundle,
                const std::string& item);

    void Invalidate(int bundle,
                    const std::string& item);

    void Store(int bundle,
               const std::string& item,
               const std::string& content);

    void SetProperty(CacheProperty property,
                     const std::string& value);

    bool LookupProperty(std::string& target,
                        CacheProperty property);
  };
}
