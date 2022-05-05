# Contribution Guidelines

If you're looking for guidelines on how to help us with mod, you found them!
We're always open to new ideas and suggestions, including code contributions.

On this page, you'll find instructions on how to set up workspace, what is our
code style and what files contain what sorts of content and code.

## Setting up workspace

### Downloading the code

If you're familiar with Git and GitHub, it would certainly be better if you
worked on local Git repo obtained with `git clone`; however, if you're not
or just feel like working without, it's fine — just let us know when you've
done your changes to the code and pass us your files.

#### Getting source code with Git CLI

You can obtain source code with Git CLI if you're comfortable with command
line:

```shell
git clone -b dev https://github.com/my-otter-self/monika_selfharm.git
# ... OR ...
git clone -b dev ssh://github.com/my-otter-self/monika_selfharm.git
```


#### Getting source code as .zip package

Alternatively, you can grab source code as .zip package — just head over
[to the main page](https://github.com/my-otter-self/monika_selfharm),
switch current branch to `dev` (this is important because we keep all the
latest changes in there before merging to `main`), click on 'Code' button
and then on 'Download ZIP'.


### Getting tools

#### Code editor

While you can actually work on the submod with any text editor (yes, `notepad.exe`
included) this doesn't mean *you should*.

Here's what you can use for easier and more comfortable work with code:

* Atom — https://atom.io/ — runs on Windows/Linux/MacOS, we recommend installing
  `language-renpy` package right after the app install so that you won't have
  some hard time working with `.rpy` files.
* Visual Studio Code — https://code.visualstudio.com/ — runs on Windows/Linux/MacOS,
  similarly to the abovementioned Atom it's recommended to get `languague-renpy`
  plugin for easier work with `.rpy` files.
* Notepad++ — https://notepad-plus-plus.org/ — runs on Windows only, basically an
  improved classic Notepad designed for better work with code.


#### Git and Git Bash (optional)

If you're using Windows or MacOS, you likely don't have Git tools installed on your
system, and on Windows you definitely don't have all the necessary utils used in
development scripts we have.

We will always accept code suggestions outside GitHub, but if you create actual pull
requests and submit code under your own name, you can get [Git tools from here](https://git-scm.org/).


## Project structure

Our project has the following structure:

```
monika_selfharm
├── [.md files, .gitignore, etc.]
├── build.env
├── mod
└── scripts
```

### /mod/

In `mod` folder there are all the script files containing dialogue lines and API code.

You may have noticed that there are (`00_header.rpy`, `script-XXXXX.rpy` and `zz_XXXXX.rpy`)
files with different prefixes. Here's why:

* `00_header.rpy` has `00_` in front of it because it is a submod header file (also
  containing submod updater header too) and it needs to be loaded before all the others.
* `script-XXXXX.rpy` files are files that contain (mostly) dialogue scripts and event
  registrations; they do not contain much code and only use APIs defined in base MAS and
  `zz_XXXXX.rpy` files.
* `zz_XXXXX.rpy` files contain APIs and the most of the actual code.

For more info, see its [README](mod/README.md).


### /scripts/

In `scripts` folder there are some useful development scripts (*sh and Python, and they require
some command line interface knowledge to handle) that might really help you out in process
of writing dialogues or code.

For more info, see its [README](scripts/README.md).


### /build.env

`build.env` file contains some environment variables that are used in submod build process.
For now it's just DDLC, MAS and Ren'Py SDK versions.

For more info, see [the comments inside of it](build.env).
