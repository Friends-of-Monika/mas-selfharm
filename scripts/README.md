# Developer Scripts

This folder contains some useful scripts to assist in submod development.
See the description of each of these below.

Scripts require POSIX shell and/or Python interpreter installed
as well as some experience of working with command line.

## hooks

`hooks` folder contains various useful Git hooks.


## compile

Lints and compiles submod package (.zip), saving it in `build/out/` folder.


## extract-strings

Extracts all strings from every `.rpy` file for reference/review.


## lint

Similar to `compile`, but only performs code linting and testing (does not package the submod.)
