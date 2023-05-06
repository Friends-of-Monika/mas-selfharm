#!/bin/sh

if [ "$#" -eq 0 ]; then
    cat <<EOF
Usage: $0 DIRECTORY
EOF
    exit 1
fi

find "$1" -type f -iname "*.json" -exec sh -c 'jq . "$0" > "$0-" && mv "$0-" "$0"' \{\} \;