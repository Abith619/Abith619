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


#include "SeriesInformationAdapter.h"

#include "ViewerToolbox.h"

#include <Logging.h>

#include <boost/regex.hpp>

namespace OrthancPlugins
{
  bool SeriesInformationAdapter::Create(std::string& content,
                                        const std::string& seriesId)
  {
    LOG(INFO) << "Ordering instances of series: " << seriesId;

    Json::Value series, study, patient, ordered;
    if (!GetJsonFromOrthanc(series, context_, "/series/" + seriesId) ||
        !GetJsonFromOrthanc(study, context_, "/studies/" + series["ID"].asString() + "/module?simplify") ||
        !GetJsonFromOrthanc(patient, context_, "/studies/" + series["ID"].asString() + "/module-patient?simplify") ||
        !GetJsonFromOrthanc(ordered, context_, "/series/" + series["ID"].asString() + "/ordered-slices") ||
        !series.isMember("Instances") ||
        series["Instances"].type() != Json::arrayValue)
    {
      return false;
    }

    Json::Value result;
    result["ID"] = seriesId;
    result["SeriesDescription"] = series["MainDicomTags"]["SeriesDescription"].asString();
    result["StudyDescription"] = study["StudyDescription"].asString();
    result["PatientID"] = patient["PatientID"].asString();
    result["PatientName"] = patient["PatientName"].asString();
    result["Type"] = ordered["Type"];
    result["Slices"] = ordered["Slices"];

    boost::regex pattern("^/instances/([a-f0-9-]+)/frames/([0-9]+)$");

    for (Json::Value::ArrayIndex i = 0; i < result["Slices"].size(); i++)
    {
      boost::cmatch what;
      if (regex_match(result["Slices"][i].asCString(), what, pattern))
      {
        result["Slices"][i] = std::string(what[1]) + "_" + std::string(what[2]);
      }
      else
      {
        return false;
      }
    }

    content = result.toStyledString();

    return true;
  }
}
