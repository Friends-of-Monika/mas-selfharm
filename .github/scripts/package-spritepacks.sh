#!/bin/sh

# Copy all spritepacks to temporary location
tmp="$(mktemp -d)"
find spritepacks -mindepth 2 -maxdepth 2 -type d -exec sh -c 'cp -r "$0" "$1/$(basename "$0")"' \{\} "$tmp" \;

# Package spritepacks
old_pwd="$PWD"
cd "$tmp"
zip -9 -q -r "spritepacks-$VERSION.zip" .

# Move spritepacks to build/out for further export/upload
cd "$old_pwd"
mv "$tmp/spritepacks-$VERSION.zip" build/out

# Remove temporary directory
rm -rf "$tmp"
