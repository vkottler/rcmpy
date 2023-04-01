<!--
    =====================================
    generator=datazen
    version=3.1.0
    hash=7fc24edd9b7b2970dad106d7fa968eb1
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

## Platform Support

This package is tested on the following platforms:

* `ubuntu-latest`
* `macos-latest`
* `windows-latest`

# Introduction

# Command-line Options

```
$ ./venv3.8/bin/rcmpy -h

usage: rcmpy [-h] [--version] [-v] [-C DIR] {apply,use,noop} ...

A configuration-file management system.

optional arguments:
  -h, --help         show this help message and exit
  --version          show program's version number and exit
  -v, --verbose      set to increase logging verbosity
  -C DIR, --dir DIR  execute from a specific directory

commands:
  {apply,use,noop}   set of available commands
    apply            apply any pending changes from the active data repository
    use              set the directory to use as the rcmpy data repository
    noop             command stub (does nothing)

```

# Internal Dependency Graph

A coarse view of the internal structure and scale of
`rcmpy`'s source.
Generated using [pydeps](https://github.com/thebjorn/pydeps) (via
`mk python-deps`).

![rcmpy's Dependency Graph](im/pydeps.svg)
