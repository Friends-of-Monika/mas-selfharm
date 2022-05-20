#!/bin/sh

# Clear MAS logs
find build/ddlc/log -type f -iname '*.log' -delete

# Copy .rpy files from mod folder
mkdir -p build/ddlc/game/mshMod
find mod -iname '*.rpy' -exec cp --parents \{\} build/ddlc/game/mshMod \;

# Move spritepacks into their respective locations
find spritepacks -mindepth 2 -maxdepth 2 -type d -exec cp -RT \{\} build/ddlc/ \;

# Run build and join build output and spj.log together
build/renpy/renpy.sh build/ddlc compile 2>&1 \
    | tee build/compile.log \
    | perl -ne 'print if (/^game\/mshMod[^\s]*: \w*Warning/ || !/^game\//)' \
    | sed 's/game\/mshMod\///g'
perl -ne 'print if (/^.*!ERROR! T_T.*$/)' build/ddlc/log/spj.log \
    | tee -a build/compile.log

# Scan for errors in log
if grep -Eq '^.*Error:.*$|^File ".*", line .*:.*$' build/compile.log; then exit 1; fi
if tail -n +9 build/ddlc/log/spj.log | grep -Eq '^.*!ERROR! T_T.*$'; then exit 1; fi

# Move compiled files to build/out
find build/ddlc/game/mshMod -type f -not -iname '*.rpyc' -delete
mkdir -p build/out/game/Submods
mv build/ddlc/game/mshMod "build/out/game/Submods/$(perl -ne 'printf $1 if /name="([^"]*)"/' "mod/00_header.rpy")"
