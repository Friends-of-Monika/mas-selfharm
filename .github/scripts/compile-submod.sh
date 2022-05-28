#!/bin/sh

# Clear MAS logs
if [ -d build/ddlc/log ]; then
    find build/ddlc/log -type f -iname '*.log' -delete
fi

# Copy .rpy files from mod folder
mkdir -p build/ddlc/game/mshMod
find mod -iname '*.rpy' -exec cp -r --parents \{\} build/ddlc/game/mshMod \;

# Move spritepacks into their respective locations
find spritepacks -mindepth 2 -maxdepth 2 -type d -exec cp -RT \{\} build/ddlc \;

# Move resources into submod folder
mkdir -p build/ddlc/game/mshMod/res
find res -exec cp -r --parents \{\} build/ddlc/game/mshMod \;

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
find build/ddlc/game/mshMod/mod -type f -not -iname '*.rpyc' -delete
mkdir -p build/out/game/Submods
mv build/ddlc/game/mshMod "build/out/game/Submods/$(perl -ne 'printf $1 if /name="([^"]*)"/' "mod/00_header.rpy")"

# Remove submod and spritepack files from build directory
rm -rf build/ddlc/game/mshMod
find spritepacks -mindepth 2 -type f -exec sh -c 'rm "build/ddlc/$(echo "$0" | sed -nE '"'s/^.*\/((game|characters)\/.*)/\1/p'"')"' \{\} \;
