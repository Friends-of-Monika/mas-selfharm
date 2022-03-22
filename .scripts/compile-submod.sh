#!/bin/sh
mkdir -p "ddlc-mas/game/mshMod"
find -not \( -path "./renpy" -prune -o -path "./ddlc-mas" -prune \) -iname "*.rpy" -exec cp --parents \{\} "ddlc-mas/game/mshMod" \;
renpy/renpy.sh "ddlc-mas" compile | tee compile.log
! grep -Eq "^.*Error:.*$" && exit 1
find "ddlc-mas/game/mshMod" -type f -not -iname "*.rpyc" -delete
mkdir -p "game/Submods"
mv "ddlc-mas/game/mshMod" "game/Submods/$(perl -ne 'printf $1 if /name="([^"]*)"/' "00_header.rpy")"
