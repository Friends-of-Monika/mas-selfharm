#!/bin/sh
if [ -d build/ddlc ]; then exit 0; fi

mkdir -p build

wget -q --show-progress --user "$(printf "%s" "$DL_CREDENTIALS" | cut -f 1 -d ":")" --password "$(printf "%s" "$DL_CREDENTIALS" | cut -f 2 -d ":")" -O build/ddlc.zip https://dl.mon.icu/stash/ddlc.zip
unzip -q build/ddlc.zip -d build/ddlc
mv build/ddlc/DDLC-1.1.1-pc build/ddlc-
rm -d build/ddlc build/ddlc.zip
mv build/ddlc- build/ddlc

wget -q --show-progress "$(curl -sL https://api.github.com/repos/monika-after-story/monikamoddev/releases/latest | perl -lne 'print $1 if /"browser_download_url": "(.+?-Mod\.zip)"/')" -O build/mas.zip
unzip -o -q build/mas.zip -d build/ddlc/game
rm -rf build/mas.zip
