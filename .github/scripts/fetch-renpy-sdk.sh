#!/bin/sh
if [ -d build/renpy ]; then exit 0; fi

mkdir -p build

wget -q --show-progress "https://www.renpy.org/dl/$RENPY_RELEASE/renpy-$RENPY_RELEASE-sdk.tar.bz2" -O "build/renpy-$RENPY_RELEASE-sdk.tar.bz2"
(cd build && tar xf "renpy-$RENPY_RELEASE-sdk.tar.bz2")
rm "build/renpy-$RENPY_RELEASE-sdk.tar.bz2"
mv "build/renpy-$RENPY_RELEASE-sdk" build/renpy
