<!--
    =====================================
    generator=datazen
    version=3.1.0
    hash=fe3e09e0d89218f917b0f128f402465c
    =====================================
-->

# rcmpy ([0.1.0](https://pypi.org/project/rcmpy/))

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
It keeps stateful information that needs to persist between command invocations
in a `rcmpy` sub-directory in the user-state directory controlled
by `XDG_STATE_HOME` (or the default: `$HOME/.local/state`).

One tracked piece of stateful information is the location of the current
[data repository](md/data_repository.md). If this is not changed (via the `use`
command), it checks a `rcmpy/default` sub-directory in the
user-config directory controlled by `XDG_CONFIG_HOME` (or the default:
`$HOME/.config`).

# Command-line Options

```
$ ./venv3.8/bin/rcmpy -h

usage: rcmpy [-h] [--version] [-v] [-C DIR] {apply,use,variant,noop} ...

A configuration-file management system.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         set to increase logging verbosity
  -C DIR, --dir DIR     execute from a specific directory

commands:
  {apply,use,variant,noop}
                        set of available commands
    apply               apply any pending changes from the active data
                        repository
    use                 set the directory to use as the rcmpy data repository
    variant             set the variant of configuration data to use
    noop                command stub (does nothing)

```

## Sub-command Options

### `apply`

```
$ ./venv3.8/bin/rcmpy apply -h

usage: rcmpy apply [-h]

optional arguments:
  -h, --help  show this help message and exit

```

### `use`

```
$ ./venv3.8/bin/rcmpy use -h

usage: rcmpy use [-h] [-d] [directory]

positional arguments:
  directory      the directory to use

optional arguments:
  -h, --help     show this help message and exit
  -d, --default  sets the directory back to the package default

```

### `variant`

```
$ ./venv3.8/bin/rcmpy variant -h

usage: rcmpy variant [-h] variant

positional arguments:
  variant     new variant to use

optional arguments:
  -h, --help  show this help message and exit

```

# Internal Dependency Graph

A coarse view of the internal structure and scale of
`rcmpy`'s source.
Generated using [pydeps](https://github.com/thebjorn/pydeps) (via
`mk python-deps`).

![rcmpy's Dependency Graph](im/pydeps.svg)
