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


cmake_minimum_required(VERSION 2.8)

project(OrthancWebViewer)

set(ORTHANC_PLUGIN_VERSION "2.7")

if (ORTHANC_PLUGIN_VERSION STREQUAL "mainline")
  set(ORTHANC_FRAMEWORK_DEFAULT_VERSION "mainline")
  set(ORTHANC_FRAMEWORK_DEFAULT_SOURCE "hg")
else()
  set(ORTHANC_FRAMEWORK_DEFAULT_VERSION "1.8.1")
  set(ORTHANC_FRAMEWORK_DEFAULT_SOURCE "web")
endif()


# Parameters of the build
set(STATIC_BUILD OFF CACHE BOOL "Static build of the third-party libraries (necessary for Windows)")
set(STANDALONE_BUILD ON CACHE BOOL "Standalone build (all the resources are embedded, necessary for releases)")
set(ALLOW_DOWNLOADS OFF CACHE BOOL "Allow CMake to download packages")
set(ORTHANC_FRAMEWORK_SOURCE "${ORTHANC_FRAMEWORK_DEFAULT_SOURCE}" CACHE STRING "Source of the Orthanc framework (can be \"system\", \"hg\", \"archive\", \"web\" or \"path\")")
set(ORTHANC_FRAMEWORK_VERSION "${ORTHANC_FRAMEWORK_DEFAULT_VERSION}" CACHE STRING "Version of the Orthanc framework")
set(ORTHANC_FRAMEWORK_ARCHIVE "" CACHE STRING "Path to the Orthanc archive, if ORTHANC_FRAMEWORK_SOURCE is \"archive\"")
set(ORTHANC_FRAMEWORK_ROOT "" CACHE STRING "Path to the Orthanc source directory, if ORTHANC_FRAMEWORK_SOURCE is \"path\"")


# Advanced parameters to fine-tune linking against system libraries
set(USE_SYSTEM_ORTHANC_SDK ON CACHE BOOL "Use the system version of the Orthanc plugin SDK")
set(ORTHANC_FRAMEWORK_STATIC OFF CACHE BOOL "If linking against the Orthanc framework system library, indicates whether this library was statically linked")
mark_as_advanced(ORTHANC_FRAMEWORK_STATIC)


# Download and setup the Orthanc framework
include(${CMAKE_SOURCE_DIR}/Resources/Orthanc/CMake/DownloadOrthancFramework.cmake)

include_directories(${ORTHANC_FRAMEWORK_ROOT})

if (ORTHANC_FRAMEWORK_SOURCE STREQUAL "system")
  link_libraries(${ORTHANC_FRAMEWORK_LIBRARIES})

  set(USE_SYSTEM_GOOGLE_TEST ON CACHE BOOL "Use the system version of Google Test")
  set(USE_GOOGLE_TEST_DEBIAN_PACKAGE OFF CACHE BOOL "Use the sources of Google Test shipped with libgtest-dev (Debian only)")
  mark_as_advanced(USE_GOOGLE_TEST_DEBIAN_PACKAGE)
  include(${CMAKE_SOURCE_DIR}/Resources/Orthanc/CMake/GoogleTestConfiguration.cmake)
else()
  include(${ORTHANC_FRAMEWORK_ROOT}/../Resources/CMake/OrthancFrameworkParameters.cmake)
  
  set(ENABLE_LOCALE OFF)         # Disable support for locales (notably in Boost)
  set(ENABLE_GOOGLE_TEST ON)
  set(ENABLE_SQLITE ON)
  set(ENABLE_MODULE_JOBS OFF CACHE INTERNAL "")
  set(ENABLE_MODULE_DICOM OFF CACHE INTERNAL "")
  
  include(${ORTHANC_FRAMEWORK_ROOT}/../Resources/CMake/OrthancFrameworkConfiguration.cmake)
endif()


include(${CMAKE_SOURCE_DIR}/Resources/CMake/JavaScriptLibraries.cmake)
include(${CMAKE_SOURCE_DIR}/Resources/Orthanc/Plugins/OrthancPluginsExports.cmake)


# Check that the Orthanc SDK headers are available
if (STATIC_BUILD OR NOT USE_SYSTEM_ORTHANC_SDK)
  include_directories(${CMAKE_SOURCE_DIR}/Resources/Orthanc/Sdk-0.9.5)
else ()
  CHECK_INCLUDE_FILE_CXX(orthanc/OrthancCPlugin.h HAVE_ORTHANC_H)
  if (NOT HAVE_ORTHANC_H)
    message(FATAL_ERROR "Please install the headers of the Orthanc plugins SDK")
  endif()
endif()


if (STANDALONE_BUILD)
  add_definitions(
    -DORTHANC_STANDALONE=1
    )
  set(EMBEDDED_RESOURCES
    WEB_VIEWER  ${CMAKE_SOURCE_DIR}/WebApplication
    )
else()
  add_definitions(
    -DORTHANC_STANDALONE=0
    -DWEB_VIEWER_PATH="${CMAKE_SOURCE_DIR}/WebApplication/"
    )
endif()

add_definitions(
  -DHAS_ORTHANC_EXCEPTION=1
  )

EmbedResources(
  ORTHANC_EXPLORER  ${CMAKE_SOURCE_DIR}/Resources/OrthancExplorer.js
  JAVASCRIPT_LIBS   ${JAVASCRIPT_LIBS_DIR}
  ${EMBEDDED_RESOURCES}
  )

if (${CMAKE_SYSTEM_NAME} STREQUAL "Linux" OR
    ${CMAKE_SYSTEM_NAME} STREQUAL "kFreeBSD" OR
    ${CMAKE_SYSTEM_NAME} STREQUAL "FreeBSD")
  link_libraries(rt)
elseif (${CMAKE_SYSTEM_NAME} STREQUAL "Windows")
  SET(CMAKE_CXX_STANDARD_LIBRARIES "${CMAKE_CXX_STANDARD_LIBRARIES} -lws2_32")

  execute_process(
    COMMAND 
    ${PYTHON_EXECUTABLE} ${ORTHANC_FRAMEWORK_ROOT}/../Resources/WindowsResources.py
    ${ORTHANC_PLUGIN_VERSION} "OrthancWebViewer" OrthancWebViewer.dll "Web viewer of medical images for Orthanc"
    ERROR_VARIABLE Failure
    OUTPUT_FILE ${AUTOGENERATED_DIR}/Version.rc
    )

  if (Failure)
    message(FATAL_ERROR "Error while computing the version information: ${Failure}")
  endif()

  list(APPEND AUTOGENERATED_SOURCES  ${AUTOGENERATED_DIR}/Version.rc)
endif()


# As the "EmbeddedResources.(h|cpp)" are shared by both the
# "UnitTests" and the "OrthancWebViewer" targets, avoid race
# conditions in the code generation by adding a target between them
add_custom_target(
  AutogeneratedTarget
  DEPENDS 
  ${AUTOGENERATED_SOURCES}
  )
          
set(CORE_SOURCES
  ${CMAKE_SOURCE_DIR}/Plugin/Cache/CacheManager.cpp
  ${CMAKE_SOURCE_DIR}/Plugin/Cache/CacheScheduler.cpp
  ${CMAKE_SOURCE_DIR}/Plugin/ViewerToolbox.cpp
  ${CMAKE_SOURCE_DIR}/Plugin/ViewerPrefetchPolicy.cpp
  ${CMAKE_SOURCE_DIR}/Plugin/SeriesInformationAdapter.cpp
  
  ${ORTHANC_CORE_SOURCES}
  )

add_library(OrthancWebViewer
  SHARED
  ${AUTOGENERATED_SOURCES}
  ${CMAKE_SOURCE_DIR}/Plugin/DecodedImageAdapter.cpp
  ${CMAKE_SOURCE_DIR}/Plugin/Plugin.cpp
  ${CORE_SOURCES}
  ${CMAKE_SOURCE_DIR}/Resources/Orthanc/Plugins/OrthancPluginCppWrapper.cpp
  )

add_dependencies(OrthancWebViewer AutogeneratedTarget)


message("Setting the version of the library to ${ORTHANC_PLUGIN_VERSION}")

add_definitions(-DORTHANC_PLUGIN_VERSION="${ORTHANC_PLUGIN_VERSION}")

set_target_properties(OrthancWebViewer PROPERTIES 
  VERSION ${ORTHANC_PLUGIN_VERSION} 
  SOVERSION ${ORTHANC_PLUGIN_VERSION})

install(
  TARGETS OrthancWebViewer
  RUNTIME DESTINATION lib    # Destination for Windows
  LIBRARY DESTINATION share/orthanc/plugins    # Destination for Linux
  )

add_executable(UnitTests
  ${AUTOGENERATED_SOURCES}
  ${CORE_SOURCES}
  ${GOOGLE_TEST_SOURCES}
  UnitTestsSources/UnitTestsMain.cpp
  )

add_dependencies(UnitTests AutogeneratedTarget)

target_link_libraries(UnitTests ${GOOGLE_TEST_LIBRARIES})
