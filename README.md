<!--
    =====================================
    generator=datazen
    version=3.1.2
    hash=744ace272d6f05ecee63ea172bf1a6bd
    =====================================
-->

# rcmpy ([1.5.1](https://pypi.org/project/rcmpy/))

[![python](https://img.shields.io/pypi/pyversions/rcmpy.svg)](https://pypi.org/project/rcmpy/)
![Build Status](https://github.com/vkottler/rcmpy/workflows/Python%20Package/badge.svg)
[![codecov](https://codecov.io/gh/vkottler/rcmpy/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/rcmpy)
![PyPI - Status](https://img.shields.io/pypi/status/rcmpy)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/rcmpy)

*A configuration-file management system.*

See also: [generated documentation](https://vkottler.github.io/python/pydoc/rcmpy.html)
(created with [`pydoc`](https://docs.python.org/3/library/pydoc.html)).

## Python Version Support

This package is tested with the following Python minor versions:

* [`python3.7`](https://docs.python.org/3.7/)
* [`python3.8`](https://docs.python.org/3.8/)
* [`python3.9`](https://docs.python.org/3.9/)
* [`python3.10`](https://docs.python.org/3.10/)
* [`python3.11`](https://docs.python.org/3.11/)

## Platform Support

This package is tested on the following platforms:

* `ubuntu-latest`
* `macos-latest`
* `windows-latest`

# Introduction

This project aims to simplify management of user configuration files, user (or
system-wide) package installations, system settings and more on a variety of
platforms.

Reasons to use it:
1. Simplify bootstrapping a fresh system to a "developer workstation" in as few
steps as possible
   1. This can be a simpler options for teams or individuals who don't have
   infrastructure to manage system-install images, system-distribution build
   systems, other kinds of provisioning automation, etc.
1. Normalize software configurations for a team of developers, but still allow
personalized overrides when desired (e.g. text-editor or terminal configs)
   1. This can help make your team or organization's development environment
   more approachable to new or inexperienced developers (ask yourself this:
   are the code changes usually even the hard part?)
1. Relies on a minimal [data repository](md/data_repository.md) that can be
managed with version control, shared by multiple people, open source to provide
examples to the community, etc.
   1. This enables a workflow for adding, removing, updating and re-configuring
   software used by a project-ecosystem over time

# Getting Started

This package attempts to adhere to the
[XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).
It keeps stateful formation that needs to persist between command invocations
in a `rcmpy` sub-directory of the user-state directory controlled
by `XDG_STATE_HOME` (or the default: `$HOME/.local/state`).

One tracked piece of stateful information is the location of the current
[data repository](md/data_repository.md). If this is not changed (via the `use`
command), it checks a `rcmpy/default` sub-directory in the
user-config directory controlled by `XDG_CONFIG_HOME` (or the default:
`$HOME/.config`).

## System Requirements

1. It is assumed that the system has a [Python](https://www.python.org/)
executable and [pip](https://pypi.org/project/pip/) is available to it as
an installed package (can be checked with: `python[3][.exe] -m pip --version`
or `pip[3][.exe] --version`).
2. A mechanism to obtain a [data repository](md/data_repository.md) via a
network connection, if one won't be created from scratch (e.g. a
[git](https://git-scm.com/) client).

## Installation and Setup

1. Install the package with `pip[3][.exe] --user rcmpy` or
`python[3][.exe] -m pip --user rcmpy`.
1. Test that `rcmpy` is now a shell command with
`rcmpy --version`.
   1. If not, you may need to invoke
   `rcmpy` directly from `$HOME/.local/bin` or
   `%APPDATA%\Python`.
(see the
[pip documentation](https://pip.pypa.io/en/stable/user_guide/?highlight=--user#user-installs)
for more info).
1. Run `rcmpy use` to view the default
[data repository](md/data_repository.md) location (printed to the console):

```
$ rcmpy use
rcmpy.state                          - INFO   - Using directory '/home/vkottler/.config/rcmpy/default'.
```

4. Begin setting up your [data repository](md/data_repository.md) in this
location, or:
   1. Download (or `git clone`) one to that default location.
   1. Create a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link) at
   that location, pointing to one.
   1. Run `rcmpy use <path>` to point `rcmpy` at
   an existing one at any arbitrary location.
5. Run `rcmpy apply` to perform tasks specified in the
[top-level configuration file](md/data_repository.md#top-level-configuration).

# Command-line Options

```
$ ./venv3.11/bin/rcmpy -h

usage: rcmpy [-h] [--version] [-v] [-C DIR]
             {apply,dump,use,variant,watch,noop} ...

A configuration-file management system.

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         set to increase logging verbosity
  -C DIR, --dir DIR     execute from a specific directory

commands:
  {apply,dump,use,variant,watch,noop}
                        set of available commands
    apply               apply any pending changes from the active data
                        repository
    dump                dump template data to stdout as JSON
    use                 set the directory to use as the rcmpy data repository
    variant             set the variant of configuration data to use
    watch               do a task whenever a file in a specified directory
                        changes
    noop                command stub (does nothing)

```

## Sub-command Options

### `apply`

```
$ ./venv3.11/bin/rcmpy apply -h

usage: rcmpy apply [-h] [-f] [-d]

options:
  -h, --help     show this help message and exit
  -f, --force    whether or not to forcibly render all outputs
  -d, --dry-run  whether or not to update output files

```

### `dump`

```
$ ./venv3.11/bin/rcmpy dump -h

usage: rcmpy dump [-h]

options:
  -h, --help  show this help message and exit

```

### `use`

```
$ ./venv3.11/bin/rcmpy use -h

usage: rcmpy use [-h] [-d] [directory]

positional arguments:
  directory      the directory to use

options:
  -h, --help     show this help message and exit
  -d, --default  sets the directory back to the package default

```

### `variant`

```
$ ./venv3.11/bin/rcmpy variant -h

usage: rcmpy variant [-h] [-d] [variant]

positional arguments:
  variant        new variant to use

options:
  -h, --help     show this help message and exit
  -d, --default  sets the directory back to the package default

```

### `watch`

```
$ ./venv3.11/bin/rcmpy watch -h

usage: rcmpy watch [-h] [-p POLL_RATE] [-s] [-i] [-n] directory cmd [cmd ...]

positional arguments:
  directory             directory to watch for file changes
  cmd                   command to run

options:
  -h, --help            show this help message and exit
  -p POLL_RATE, --poll-rate POLL_RATE
                        poll period in seconds (default: 0.1s)
  -s, --shell           set to run a shell command
  -i, --single-pass     only run a single iteration
  -n, --no-change       don't act on changed files, only the overall set of
                        files changing (added or removed)

```

# Internal Dependency Graph

A coarse view of the internal structure and scale of
`rcmpy`'s source.
Generated using [pydeps](https://github.com/thebjorn/pydeps) (via
`mk python-deps`).

![rcmpy's Dependency Graph](im/pydeps.svg)
