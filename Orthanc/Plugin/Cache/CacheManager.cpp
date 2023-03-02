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


#include "CacheManager.h"

#include <Compatibility.h>
#include <Toolbox.h>
#include <SQLite/Transaction.h>

#include <boost/lexical_cast.hpp>


namespace OrthancPlugins
{
  class CacheManager::Bundle
  {
  private:
    uint32_t  count_;
    uint64_t  space_;

  public:
    Bundle() : count_(0), space_(0)
    {
    }

    Bundle(uint32_t count,
           uint64_t space) : 
      count_(count), space_(space)
    {
    }

    uint32_t GetCount() const
    {
      return count_;
    }

    uint64_t GetSpace() const
    {
      return space_;
    }

    void Remove(uint64_t fileSize)
    {
      if (count_ == 0 ||
          space_ < fileSize)
      {
        throw std::runtime_error("Internal error");
      }

      count_ -= 1;
      space_ -= fileSize;
    }

    void Add(uint64_t fileSize)
    {
      count_ += 1;
      space_ += fileSize;
    }
  };


  class CacheManager::BundleQuota
  {
  private:   
    uint32_t maxCount_;
    uint64_t maxSpace_;

  public:
    BundleQuota(uint32_t maxCount,
                uint64_t maxSpace) : 
      maxCount_(maxCount), maxSpace_(maxSpace)
    {
    }

    BundleQuota()
    {
      // Default quota
      maxCount_ = 0;  // No limit on the number of files
      maxSpace_ = 100 * 1024 * 1024;  // Max 100MB per bundle
    }

    uint32_t GetMaxCount() const
    {
      return maxCount_;
    }

    uint64_t GetMaxSpace() const
    {
      return maxSpace_;
    }

    bool IsSatisfied(const Bundle& bundle) const
    {
      if (maxCount_ != 0 &&
          bundle.GetCount() > maxCount_)
      {
        return false;
      }

      if (maxSpace_ != 0 &&
          bundle.GetSpace() > maxSpace_)
      {
        return false;
      }

      return true;
    }
  };


  struct CacheManager::PImpl
  {
    OrthancPluginContext* context_;
    Orthanc::SQLite::Connection& db_;
    Orthanc::FilesystemStorage& storage_;

    bool sanityCheck_;
    Bundles  bundles_;
    BundleQuota  defaultQuota_;
    BundleQuotas  quotas_;

    PImpl(OrthancPluginContext* context,
          Orthanc::SQLite::Connection& db,
          Orthanc::FilesystemStorage& storage) :
      context_(context),
      db_(db), 
      storage_(storage), 
      sanityCheck_(false)
    {
    }
  };


  const CacheManager::BundleQuota& CacheManager::GetBundleQuota(int bundleIndex) const
  {
    BundleQuotas::const_iterator found = pimpl_->quotas_.find(bundleIndex);

    if (found == pimpl_->quotas_.end())
    {
      return pimpl_->defaultQuota_;
    }
    else
    {
      return found->second;
    }
  }


  CacheManager::Bundle CacheManager::GetBundle(int bundleIndex) const
  {
    Bundles::const_iterator it = pimpl_->bundles_.find(bundleIndex);
  
    if (it == pimpl_->bundles_.end())
    {
      return Bundle();
    }
    else
    {
      return it->second;
    }
  }


  void CacheManager::MakeRoom(Bundle& bundle,
                              std::list<std::string>& toRemove,
                              int bundleIndex,
                              const BundleQuota& quota)
  {
    using namespace Orthanc;

    toRemove.clear();

    // Make room in the bundle
    while (!quota.IsSatisfied(bundle))
    {
      SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT seq, fileUuid, fileSize FROM Cache WHERE bundle=? ORDER BY seq");
      s.BindInt(0, bundleIndex);

      if (s.Step())
      {
        SQLite::Statement t(pimpl_->db_, SQLITE_FROM_HERE, "DELETE FROM Cache WHERE seq=?");
        t.BindInt64(0, s.ColumnInt64(0));
        t.Run();

        toRemove.push_back(s.ColumnString(1));
        bundle.Remove(s.ColumnInt64(2));
      }
      else
      {
        // Should never happen
        throw std::runtime_error("Internal error");
      }
    }
  }



  void CacheManager::EnsureQuota(int bundleIndex,
                                 const BundleQuota& quota)
  {
    using namespace Orthanc;

    // Remove the cached files that exceed the quota
    std::unique_ptr<SQLite::Transaction> transaction(new SQLite::Transaction(pimpl_->db_));
    transaction->Begin();

    Bundle bundle = GetBundle(bundleIndex);

    std::list<std::string> toRemove;
    MakeRoom(bundle, toRemove, bundleIndex, quota);

    transaction->Commit();
    for (std::list<std::string>::const_iterator
           it = toRemove.begin(); it != toRemove.end(); ++it)
    {
      pimpl_->storage_.Remove(*it, Orthanc::FileContentType_Unknown);
    }

    pimpl_->bundles_[bundleIndex] = bundle;
  }



  void CacheManager::ReadBundleStatistics()
  {
    using namespace Orthanc;

    pimpl_->bundles_.clear();

    SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT bundle,COUNT(*),SUM(fileSize) FROM Cache GROUP BY bundle");
    while (s.Step())
    {
      int index = s.ColumnInt(0);
      Bundle bundle(static_cast<uint32_t>(s.ColumnInt(1)),
                    static_cast<uint64_t>(s.ColumnInt64(2)));
      pimpl_->bundles_[index] = bundle;
    }
  }



  void CacheManager::SanityCheck()
  {
    if (!pimpl_->sanityCheck_)
    {
      return;
    }

    using namespace Orthanc;

    SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT bundle,COUNT(*),SUM(fileSize) FROM Cache GROUP BY bundle");
    while (s.Step())
    {
      const Bundle& bundle = GetBundle(s.ColumnInt(0));
      if (bundle.GetCount() != static_cast<uint32_t>(s.ColumnInt(1)) ||
          bundle.GetSpace() != static_cast<uint64_t>(s.ColumnInt64(2)))
      {
        throw std::runtime_error("SANITY ERROR in cache: " + boost::lexical_cast<std::string>(bundle.GetCount()) 
                                 + "/" + boost::lexical_cast<std::string>(bundle.GetSpace())
                                 + " vs " + boost::lexical_cast<std::string>(s.ColumnInt(1)) + "/"
                                 + boost::lexical_cast<std::string>(s.ColumnInt64(2)));
      }
    }
  }



  CacheManager::CacheManager(OrthancPluginContext* context,
                             Orthanc::SQLite::Connection& db,
                             Orthanc::FilesystemStorage& storage) :
    pimpl_(new PImpl(context, db, storage))
  {
    Open();
    ReadBundleStatistics();
  }


  OrthancPluginContext* CacheManager::GetPluginContext() const
  {
    return pimpl_->context_;
  }


  void CacheManager::SetSanityCheckEnabled(bool enabled)
  {
    pimpl_->sanityCheck_ = enabled;
  }


  void CacheManager::Open()
  {
    if (!pimpl_->db_.DoesTableExist("Cache"))
    {
      pimpl_->db_.Execute("CREATE TABLE Cache(seq INTEGER PRIMARY KEY, bundle INTEGER, item TEXT, fileUuid TEXT, fileSize INT);");
      pimpl_->db_.Execute("CREATE INDEX CacheBundles ON Cache(bundle);");
      pimpl_->db_.Execute("CREATE INDEX CacheIndex ON Cache(bundle, item);");
    }

    if (!pimpl_->db_.DoesTableExist("CacheProperties"))
    {
      pimpl_->db_.Execute("CREATE TABLE CacheProperties(property INTEGER PRIMARY KEY, value TEXT);");
    }

    // Performance tuning of SQLite with PRAGMAs
    // http://www.sqlite.org/pragma.html
    pimpl_->db_.Execute("PRAGMA SYNCHRONOUS=OFF;");
    pimpl_->db_.Execute("PRAGMA JOURNAL_MODE=WAL;");
    pimpl_->db_.Execute("PRAGMA LOCKING_MODE=EXCLUSIVE;");
  }


  void CacheManager::Store(int bundleIndex,
                           const std::string& item,
                           const std::string& content)
  {
    SanityCheck();

    const BundleQuota quota = GetBundleQuota(bundleIndex);

    if (quota.GetMaxSpace() > 0 &&
        content.size() > quota.GetMaxSpace())
    {
      // Cannot store such a large instance into the cache, forget about it
      return;
    }

    using namespace Orthanc;

    std::unique_ptr<SQLite::Transaction> transaction(new SQLite::Transaction(pimpl_->db_));
    transaction->Begin();

    Bundle bundle = GetBundle(bundleIndex);

    std::list<std::string>  toRemove;
    bundle.Add(content.size());
    MakeRoom(bundle, toRemove, bundleIndex, quota);

    // Store the cached content on the disk
    const char* data = content.size() ? &content[0] : NULL;
    std::string uuid = Toolbox::GenerateUuid();
    pimpl_->storage_.Create(uuid, data, content.size(), Orthanc::FileContentType_Unknown);

    // Remove the previous cached value. This might happen if the same
    // item is accessed very quickly twice: Another factory could have
    // been cached a value before the check for existence in Access().
    {
      SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT seq, fileUuid, fileSize FROM Cache WHERE bundle=? AND item=?");
      s.BindInt(0, bundleIndex);
      s.BindString(1, item);
      if (s.Step())
      {
        SQLite::Statement t(pimpl_->db_, SQLITE_FROM_HERE, "DELETE FROM Cache WHERE seq=?");
        t.BindInt64(0, s.ColumnInt64(0));
        t.Run();

        toRemove.push_back(s.ColumnString(1));
        bundle.Remove(s.ColumnInt64(2));
      }
    }

    {
      SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "INSERT INTO Cache VALUES(NULL, ?, ?, ?, ?)");
      s.BindInt(0, bundleIndex);
      s.BindString(1, item);
      s.BindString(2, uuid);
      s.BindInt64(3, content.size());

      if (!s.Run())
      {
        // Error: Remove the stored file
        pimpl_->storage_.Remove(uuid, Orthanc::FileContentType_Unknown);
      }
      else
      {
        transaction->Commit();

        pimpl_->bundles_[bundleIndex] = bundle;
    
        for (std::list<std::string>::const_iterator
               it = toRemove.begin(); it != toRemove.end(); ++it)
        {
          pimpl_->storage_.Remove(*it, Orthanc::FileContentType_Unknown);
        }
      }
    }

    SanityCheck();
  }



  bool CacheManager::LocateInCache(std::string& uuid,
                                   uint64_t& size,
                                   int bundle,
                                   const std::string& item)
  {
    using namespace Orthanc;
    SanityCheck();

    std::unique_ptr<SQLite::Transaction> transaction(new SQLite::Transaction(pimpl_->db_));
    transaction->Begin();

    SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT seq, fileUuid, fileSize FROM Cache WHERE bundle=? AND item=?");
    s.BindInt(0, bundle);
    s.BindString(1, item);
    if (!s.Step())
    {
      return false;
    }

    int64_t seq = s.ColumnInt64(0);
    uuid = s.ColumnString(1);
    size = s.ColumnInt64(2);

    // Touch the cache to fulfill the LRU scheme.
    SQLite::Statement t(pimpl_->db_, SQLITE_FROM_HERE, "DELETE FROM Cache WHERE seq=?");
    t.BindInt64(0, seq);
    if (t.Run())
    {
      SQLite::Statement u(pimpl_->db_, SQLITE_FROM_HERE, "INSERT INTO Cache VALUES(NULL, ?, ?, ?, ?)");
      u.BindInt(0, bundle);
      u.BindString(1, item);
      u.BindString(2, uuid);
      u.BindInt64(3, size);
      if (u.Run())
      {
        // Everything was OK. Commit the changes to the cache.
        transaction->Commit();
        return true;
      }
    }

    return false;
  }


  bool CacheManager::IsCached(int bundle,
                              const std::string& item)
  {
    std::string uuid;
    uint64_t size;
    return LocateInCache(uuid, size, bundle, item);
  }


  bool CacheManager::Access(std::string& content,
                            int bundle,
                            const std::string& item)
  {
    std::string uuid;
    uint64_t size;
    if (!LocateInCache(uuid, size, bundle, item))
    {
      return false;
    }

    bool ok;
    try
    {
      pimpl_->storage_.Read(content, uuid, Orthanc::FileContentType_Unknown);
      ok = (content.size() == size);
    }
    catch (std::runtime_error&)
    {
      ok = false;
    }

    if (ok)
    {
      return true;
    }
    else
    {
      throw std::runtime_error("Error in the filesystem");
    }
  }


  void CacheManager::Invalidate(int bundleIndex,
                                const std::string& item)
  {
    using namespace Orthanc;
    SanityCheck();

    std::unique_ptr<SQLite::Transaction> transaction(new SQLite::Transaction(pimpl_->db_));
    transaction->Begin();

    Bundle bundle = GetBundle(bundleIndex);

    SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT seq, fileUuid, fileSize FROM Cache WHERE bundle=? AND item=?");
    s.BindInt(0, bundleIndex);
    s.BindString(1, item);
    if (s.Step())
    {
      int64_t seq = s.ColumnInt64(0);
      const std::string uuid = s.ColumnString(1);
      uint64_t expectedSize = s.ColumnInt64(2);
      bundle.Remove(expectedSize);

      SQLite::Statement t(pimpl_->db_, SQLITE_FROM_HERE, "DELETE FROM Cache WHERE seq=?");
      t.BindInt64(0, seq);
      if (t.Run())
      {
        transaction->Commit();
        pimpl_->bundles_[bundleIndex] = bundle;
        pimpl_->storage_.Remove(uuid, Orthanc::FileContentType_Unknown);
      }
    }
  }



  void CacheManager::SetBundleQuota(int bundle,
                                    uint32_t maxCount,
                                    uint64_t maxSpace)
  {
    SanityCheck();

    const BundleQuota quota(maxCount, maxSpace);
    EnsureQuota(bundle, quota);
    pimpl_->quotas_[bundle] = quota;

    SanityCheck();
  }

  void CacheManager::SetDefaultQuota(uint32_t maxCount,
                                     uint64_t maxSpace)
  {
    using namespace Orthanc;
    SanityCheck();

    pimpl_->defaultQuota_ = BundleQuota(maxCount, maxSpace);

    SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT DISTINCT bundle FROM Cache");
    while (s.Step())
    {
      EnsureQuota(s.ColumnInt(0), pimpl_->defaultQuota_);
    }

    SanityCheck();
  }


  void CacheManager::Clear()
  {
    using namespace Orthanc;
    SanityCheck();

    SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT fileUuid FROM Cache");
    while (s.Step())
    {
      pimpl_->storage_.Remove(s.ColumnString(0), Orthanc::FileContentType_Unknown);
    }  

    SQLite::Statement t(pimpl_->db_, SQLITE_FROM_HERE, "DELETE FROM Cache");
    t.Run();

    ReadBundleStatistics();
    SanityCheck();
  }



  void CacheManager::Clear(int bundle)
  {
    using namespace Orthanc;
    SanityCheck();

    SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, "SELECT fileUuid FROM Cache WHERE bundle=?");
    s.BindInt(0, bundle);
    while (s.Step())
    {
      pimpl_->storage_.Remove(s.ColumnString(0), Orthanc::FileContentType_Unknown);
    }  

    SQLite::Statement t(pimpl_->db_, SQLITE_FROM_HERE, "DELETE FROM Cache WHERE bundle=?");
    t.BindInt(0, bundle);
    t.Run();

    ReadBundleStatistics();
    SanityCheck();
  }


  void CacheManager::SetProperty(CacheProperty property,
                                 const std::string& value)
  {
    Orthanc::SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE,
                                 "INSERT OR REPLACE INTO CacheProperties VALUES(?, ?)");
    s.BindInt(0, property);
    s.BindString(1, value);
    s.Run();
  }


  bool CacheManager::LookupProperty(std::string& target,
                                    CacheProperty property)
  {
    Orthanc::SQLite::Statement s(pimpl_->db_, SQLITE_FROM_HERE, 
                                 "SELECT value FROM CacheProperties WHERE property=?");
    s.BindInt(0, property);

    if (!s.Step())
    {
      return false;
    }
    else
    {
      target = s.ColumnString(0);
      return true;
    }
  }
}
