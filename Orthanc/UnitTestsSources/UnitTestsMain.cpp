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


#include <gtest/gtest.h>
#include <boost/lexical_cast.hpp>

static int argc_;
static char** argv_;

#include "../Plugin/Cache/CacheManager.h"
#include "../Plugin/Cache/CacheScheduler.h"
#include "../Plugin/Cache/ICacheFactory.h"
#include "../Plugin/Cache/ICacheFactory.h"

#include <Compatibility.h>
#include <Logging.h>
#include <OrthancException.h>
#include <SystemToolbox.h>

using namespace OrthancPlugins;


class CacheManagerTest : public testing::Test
{
private:
  std::unique_ptr<Orthanc::FilesystemStorage>  storage_;
  std::unique_ptr<Orthanc::SQLite::Connection>  db_;
  std::unique_ptr<CacheManager>  cache_;

public:
  virtual void SetUp()
  {
    storage_.reset(new Orthanc::FilesystemStorage("UnitTestsResults"));
    storage_->Clear();
    Orthanc::SystemToolbox::RemoveFile("UnitTestsResults/cache.db");

    db_.reset(new Orthanc::SQLite::Connection());
    db_->Open("UnitTestsResults/cache.db");

    cache_.reset(new CacheManager(NULL, *db_, *storage_));
    cache_->SetSanityCheckEnabled(true);
  }

  virtual void TearDown()
  {
    cache_.reset(NULL);
    db_.reset(NULL);
    storage_.reset(NULL);
  }

  CacheManager& GetCache() 
  {
    return *cache_;
  }

  Orthanc::FilesystemStorage& GetStorage() 
  {
    return *storage_;
  }
};



class TestF : public ICacheFactory
{
private:
  int bundle_;
  
public:
  explicit TestF(int bundle) : bundle_(bundle)
  {
  }

  virtual bool Create(std::string& content,
                      const std::string& key) ORTHANC_OVERRIDE
  {
    content = "Bundle " + boost::lexical_cast<std::string>(bundle_) + ", item " + key;
    return true;
  }
};


TEST_F(CacheManagerTest, DefaultQuota)
{
  std::set<std::string> f;
  GetStorage().ListAllFiles(f);
  ASSERT_EQ(0u, f.size());
  
  GetCache().SetDefaultQuota(10, 0);
  for (unsigned int i = 0; i < 30; i++)
  {
    GetStorage().ListAllFiles(f);
    ASSERT_EQ(i >= 10 ? 10u : i, f.size());
    std::string s = boost::lexical_cast<std::string>(i);
    GetCache().Store(0, s, "Test " + s);
  }

  GetStorage().ListAllFiles(f);
  ASSERT_EQ(10u, f.size());

  for (int i = 0; i < 30; i++)
  {
    ASSERT_EQ(i >= 20, GetCache().IsCached(0, boost::lexical_cast<std::string>(i)));
  }

  GetCache().SetDefaultQuota(5, 0);
  GetStorage().ListAllFiles(f);
  ASSERT_EQ(5u, f.size());
  for (int i = 0; i < 30; i++)
  {
    ASSERT_EQ(i >= 25, GetCache().IsCached(0, boost::lexical_cast<std::string>(i)));
  }

  for (int i = 0; i < 15; i++)
  {
    std::string s = boost::lexical_cast<std::string>(i);
    GetCache().Store(0, s, "Test " + s);
  }

  GetStorage().ListAllFiles(f);
  ASSERT_EQ(5u, f.size());

  for (int i = 0; i < 50; i++)
  {
    std::string s = boost::lexical_cast<std::string>(i);
    if (i >= 10 && i < 15)
    {
      std::string tmp;
      ASSERT_TRUE(GetCache().IsCached(0, s));
      ASSERT_TRUE(GetCache().Access(tmp, 0, s));
      ASSERT_EQ("Test " + s, tmp);
    }
    else
    {
      ASSERT_FALSE(GetCache().IsCached(0, s));
    }
  }
}



TEST_F(CacheManagerTest, Invalidate)
{
  GetCache().SetDefaultQuota(10, 0);
  for (int i = 0; i < 30; i++)
  {
    std::string s = boost::lexical_cast<std::string>(i);
    GetCache().Store(0, s, "Test " + s);
  }

  std::set<std::string> f;
  GetStorage().ListAllFiles(f);
  ASSERT_EQ(10u, f.size());

  GetCache().Invalidate(0, "25");
  GetStorage().ListAllFiles(f);
  ASSERT_EQ(9u, f.size());
  for (int i = 0; i < 50; i++)
  {
    std::string s = boost::lexical_cast<std::string>(i);
    ASSERT_EQ((i >= 20 && i < 30 && i != 25), GetCache().IsCached(0, s));
  }

  for (int i = 0; i < 50; i++)
  {
    GetCache().Invalidate(0, boost::lexical_cast<std::string>(i));
  }

  GetStorage().ListAllFiles(f);
  ASSERT_EQ(0u, f.size());
}



int main(int argc, char **argv)
{
  argc_ = argc;
  argv_ = argv;  

  ::testing::InitGoogleTest(&argc, argv);

  /*Orthanc::Logging::Initialize();
    Orthanc::Logging::EnableInfoLevel(true);*/

  return RUN_ALL_TESTS();
}
