# Orthanc - A Lightweight, RESTful DICOM Store
# Copyright (C) 2012-2016 Sebastien Jodogne, Medical Physics
# Department, University Hospital of Liege, Belgium
# Copyright (C) 2017-2020 Osimis S.A., Belgium
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


set(BASE_URL "http://orthanc.osimis.io/ThirdPartyDownloads/web-viewer")

DownloadPackage(
  "dbf236ede85e7b7871c9a42edad16d81"
  "${BASE_URL}/cornerstone-0.11.0.zip"
  "${CMAKE_CURRENT_BINARY_DIR}/cornerstone-0.11.0")

DownloadPackage(
  "cb943ac26be9ee755e8741ea232389e2"
  "${BASE_URL}/jquery-ui-1.11.3.zip"
  "${CMAKE_CURRENT_BINARY_DIR}/jquery-ui-1.11.3")

DownloadPackage(
  "169c56338f9ff812cae3e91ef72bda2e"
  "${BASE_URL}/jsPanel-2.3.3-fixed.zip"
  "${CMAKE_CURRENT_BINARY_DIR}/jspanel")

DownloadPackage(
  "8392ad105d913c3a83a7787c8f148055"
  "${BASE_URL}/pako-0.2.5.zip"
  "${CMAKE_CURRENT_BINARY_DIR}/pako-0.2.5")

DownloadPackage(
  "7ebea0b624cd62445a124d264dfa2a53"
  "${BASE_URL}/js-url-1.8.6.zip"
  "${CMAKE_CURRENT_BINARY_DIR}/js-url-1.8.6")


set(JAVASCRIPT_LIBS_DIR  ${CMAKE_CURRENT_BINARY_DIR}/javascript-libs)
file(MAKE_DIRECTORY ${JAVASCRIPT_LIBS_DIR})

file(COPY
  ${CMAKE_CURRENT_BINARY_DIR}/cornerstone-0.11.0/example/cornerstone.css
  ${CMAKE_CURRENT_BINARY_DIR}/cornerstone-0.11.0/dist/cornerstone.min.js
  ${CMAKE_CURRENT_BINARY_DIR}/jquery-ui-1.11.3/external/jquery/jquery.js
  ${CMAKE_CURRENT_BINARY_DIR}/jquery-ui-1.11.3/images
  ${CMAKE_CURRENT_BINARY_DIR}/jquery-ui-1.11.3/jquery-ui.min.css
  ${CMAKE_CURRENT_BINARY_DIR}/jquery-ui-1.11.3/jquery-ui.min.js
  ${CMAKE_CURRENT_BINARY_DIR}/jquery-ui-1.11.3/jquery-ui.theme.min.css
  ${CMAKE_CURRENT_BINARY_DIR}/js-url-1.8.6/url.min.js
  ${CMAKE_CURRENT_BINARY_DIR}/jspanel/fonts
  ${CMAKE_CURRENT_BINARY_DIR}/jspanel/images
  ${CMAKE_CURRENT_BINARY_DIR}/jspanel/jquery.jspanel.min.css
  ${CMAKE_CURRENT_BINARY_DIR}/jspanel/jquery.jspanel.min.js
  ${CMAKE_CURRENT_BINARY_DIR}/vendor/jquery.ui.touch-punch.min.js
  ${CMAKE_CURRENT_BINARY_DIR}/vendor/mobile-detect.min.js
  ${CMAKE_CURRENT_BINARY_DIR}/pako-0.2.5/dist/pako_inflate.min.js
  DESTINATION
  ${JAVASCRIPT_LIBS_DIR}
  )
