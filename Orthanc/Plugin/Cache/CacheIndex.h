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

#include <IDynamicObject.h>

#include <string>

namespace OrthancPlugins
{
  class CacheIndex : public Orthanc::IDynamicObject
  {
  private:
    int          bundle_;
    std::string  item_;

    void operator= (const CacheIndex&);  // Forbidden

  public:
    CacheIndex(const CacheIndex& other) :
      bundle_(other.bundle_),
      item_(other.item_)
    {
    }

    CacheIndex(int bundle,
               const std::string& item) :
      bundle_(bundle),
      item_(item)
    {
    }

    int GetBundle() const
    {
      return bundle_;
    }

    const std::string& GetItem() const
    {
      return item_;
    }

    bool operator== (const CacheIndex& other) const
    {
      return (bundle_ == other.bundle_ &&
              item_ == other.item_);
    }
  };
}
