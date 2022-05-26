#!/bin/sh
tmp="$(mktemp -d)"
find spritepacks -mindepth 2 -maxdepth 2 -type d -exec sh -c 'cp -r "$0" "$1/$(basename "$0")"' \{\} "$tmp" \;
old_pwd="$PWD"
cd "$tmp"
zip -9 -r "spritepacks-$VERSION.zip" .
cd "$old_pwd"
mv "$tmp/spritepacks-$VERSION.zip" build/out
rm -rf "$tmp"
