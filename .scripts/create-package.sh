#!/bin/sh
find . -not \( \
  -path ./.git -prune -o \
  -path ./.github -prune -o \
  -path ./.scripts -prune \
\) | zip msh-mod-$VERSION.zip -9 -@
