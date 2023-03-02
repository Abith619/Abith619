#!/bin/bash

##
## This script compiles cross-distribution Linux binaries thanks to
## Holy Build Box: https://github.com/phusion/holy-build-box
##
## The ideal solution would be to use Linux Standard Base
## (LSB). Unfortunately, the LSB C++ compiler is a pre-4.8 gcc that
## does not feature full C++11 capabilities, which prevents compiling
## GDCM >= 3.0.
##

set -ex

if [ "$1" != "Debug" -a "$1" != "Release" ]; then
    echo "Please provide build type: Debug or Release"
    exit -1
fi

if [ -t 1 ]; then
    # TTY is available => use interactive mode
    DOCKER_FLAGS='-i'
fi

ROOT_DIR=`dirname $(readlink -f $0)`/..

mkdir -p ${ROOT_DIR}/holy-build-box

docker run -t ${DOCKER_FLAGS} --rm \
    --user $(id -u):$(id -g) \
    -v ${ROOT_DIR}:/source:ro \
    -v ${ROOT_DIR}/holy-build-box:/target:rw \
    phusion/holy-build-box-64:2.0.1 \
    bash /source/Resources/holy-build-box-internal.sh $1

ls -lR ${ROOT_DIR}/holy-build-box/
