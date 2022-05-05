# Git hooks

This folder contains some useful Git hooks to assist in submod development.
See the description of each of these below.

Each hook is generally installed by copying it into `.git/hooks` folder under certain name.
See description and install instructions for each of these below.


## lint-before-commit

Runs `scripts/lint` before committing, ensuring that all `.rpy` files have valid syntax.
Does nothing if no `.rpy` files were changed.

### Installation

Copy into `.git/hooks` and rename into `pre-commit`.
