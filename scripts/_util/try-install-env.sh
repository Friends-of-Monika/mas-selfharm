#!/bin/sh
set -e

scripts/_util/warn-on-missing-sdk.sh
export $(awk '!/^#/{print}' < build.env | xargs)

echo "# Download DDLC/MAS package"
.github/scripts/fetch-ddlc-mas.sh

echo "# Download Ren'Py SDK"
.github/scripts/fetch-renpy-sdk.sh
