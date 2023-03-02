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

#include <Images/ImageAccessor.h>

#include <string>
#include <json/value.h>
#include <orthanc/OrthancCPlugin.h>

namespace OrthancPlugins
{
  enum CacheBundle
  {
    CacheBundle_DecodedImage = 1,
    CacheBundle_InstanceInformation = 2,
    CacheBundle_SeriesInformation = 3
  };

  bool GetStringFromOrthanc(std::string& content,
                            OrthancPluginContext* context,
                            const std::string& uri);

  bool GetJsonFromOrthanc(Json::Value& json,
                          OrthancPluginContext* context,
                          const std::string& uri);

  bool TokenizeVector(std::vector<float>& result,
                      const std::string& value,
                      unsigned int expectedSize);

  void CompressUsingDeflate(std::string& compressed,
                            OrthancPluginContext* context,
                            const void* uncompressed,
                            size_t uncompressedSize);

  const char* GetMimeType(const std::string& path);

  bool ReadConfiguration(Json::Value& configuration,
                         OrthancPluginContext* context);

  std::string GetStringValue(const Json::Value& configuration,
                             const std::string& key,
                             const std::string& defaultValue);

  int GetIntegerValue(const Json::Value& configuration,
                      const std::string& key,
                      int defaultValue);



  OrthancPluginPixelFormat Convert(Orthanc::PixelFormat format);

  Orthanc::PixelFormat Convert(OrthancPluginPixelFormat format);

  void WriteJpegToMemory(std::string& result,
                         OrthancPluginContext* context,
                         const Orthanc::ImageAccessor& accessor,
                         uint8_t quality);
 
  class ImageReader
  {
  private:
    OrthancPluginContext* context_;
    OrthancPluginImage*   image_;

  public:
    ImageReader(OrthancPluginContext* context,
                const std::string& image,
                OrthancPluginImageFormat format);

    ~ImageReader();

    void GetAccessor(Orthanc::ImageAccessor& target) const;
  };
}
