#!/bin/sh
if { ! [ -d build/ddlc ] && [ -d build/renpy ]; } && [ -z "$DL_CREDENTIALS" ]; then
    echo "# DDLC (with MAS installed) or Ren'Py SDK is missing!"
    echo "# Both are necessary for this compile/lint script to function."
    echo "# Install DDLC (with MAS) into build/ddlc and Ren'Py SDK into build/renpy manually,"
    echo "# or run this script (just once) with \$DL_CREDENTIALS environment variable set."
    exit 1
fi
