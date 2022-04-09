#!/bin/sh
set -e

echo "# Download DDLC/MAS package"
.github/scripts/fetch-ddlc-mas.sh

echo "# Download Ren'Py SDK"
.github/scripts/fetch-renpy-sdk.sh

echo "# Store submod version in an environment variable"
VERSION="$(.github/scripts/extract-version.sh)"

echo "# Compile submod"
.github/scripts/compile-submod.sh
