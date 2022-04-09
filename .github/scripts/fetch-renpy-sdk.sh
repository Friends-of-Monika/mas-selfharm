#!/bin/sh
if [ -d build/renpy ]; then exit 0; fi

mkdir -p build

wget -q --show-progress https://www.renpy.org/dl/6.99.12.4/renpy-6.99.12.4-sdk.tar.bz2 -O build/renpy-6.99.12.4-sdk.tar.bz2
(cd build && tar xf renpy-6.99.12.4-sdk.tar.bz2)
rm build/renpy-6.99.12.4-sdk.tar.bz2
mv build/renpy-6.99.12.4-sdk build/renpy
