#!/bin/sh
mkdir -p "build/ddlc/game/mshMod"
find -not \( -path "./build" -prune \) -iname "*.rpy" -exec cp --parents \{\} "build/ddlc/game/mshMod" \;
build/renpy/renpy.sh "build/ddlc" compile 2>&1 | tee build/compile.log | perl -ne 'print if (/^game\/mshMod[^\s]*: \w*Warning/ || !/^game\//)' | sed 's/game\/mshMod\///g'
if grep -Eq '^.*Error:.*$|^File ".*", line .*:.*$' build/compile.log; then exit 1; fi
find "build/ddlc/game/mshMod" -type f -not -iname "*.rpyc" -delete
mkdir -p "build/out/game/Submods"
mv "build/ddlc/game/mshMod" "build/out/game/Submods/$(perl -ne 'printf $1 if /name="([^"]*)"/' "mod/00_header.rpy")"
