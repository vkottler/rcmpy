"""
A module for working with the XDG base directory specification.

https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
"""

# built-in
from os import environ
from os import path as _path
from pathlib import Path
from typing import Iterator


def ensure_absolute(path: Path, create: bool = False) -> Path:
    """A wrapper to ensure that a path is an absolute one."""

    assert path.is_absolute(), f"'{path}' isn't absolute!"

    if create:
        path.mkdir(mode=0o700, parents=True, exist_ok=True)

    return path


def user_data(create: bool = True) -> Path:
    """
    A single base directory relative to which user-specific data files should
    be written.
    """

    return ensure_absolute(
        Path(
            environ.get(
                "XDG_DATA_HOME", Path.home().joinpath(".local", "share")
            )
        ),
        create=create,
    )


def user_config(create: bool = True) -> Path:
    """
    A single base directory relative to which user-specific configuration files
    should be written.
    """

    return ensure_absolute(
        Path(environ.get("XDG_CONFIG_HOME", Path.home().joinpath(".config"))),
        create=create,
    )


def user_state(create: bool = True) -> Path:
    """
    A single base directory relative to which user-specific state data
    should be written.
    """

    return ensure_absolute(
        Path(
            environ.get(
                "XDG_STATE_HOME", Path.home().joinpath(".local", "state")
            )
        ),
        create=create,
    )


def user_bin(create: bool = True) -> Path:
    """
    A single base directory relative to which user-specific executable files
    may be written.
    """

    return ensure_absolute(
        Path.home().joinpath(".local", "bin"), create=create
    )


def iterate_directories(
    data: str, sep: str = ":", create: bool = False
) -> Iterator[Path]:
    """
    Iterate over directories specified in a PATH-like variable (some
    separator).
    """

    for item in data.split(sep):
        yield ensure_absolute(Path(item), create=create)


def data_directories(include_home: bool = True) -> Iterator[Path]:
    """
    Yield a set of preference ordered base directories relative to which
    data files should be searched.
    """

    if include_home:
        yield user_data()

    yield from iterate_directories(
        environ.get(
            "XDG_DATA_DIRS",
            ":".join(
                [
                    str(Path(_path.sep, "share")),
                    str(Path(_path.sep, "local", "share")),
                ]
            ),
        )
    )


def config_directories(include_home: bool = True) -> Iterator[Path]:
    """
    Yield a set of preference ordered base directories relative to which
    configuration files should be searched.
    """

    if include_home:
        yield user_config()

    yield from iterate_directories(
        environ.get("XDG_CONFIG_DIRS", str(Path(_path.sep, "etc", "xdg")))
    )


def user_cache(create: bool = True) -> Path:
    """
    A single base directory relative to which user-specific
    non-essential (cached) data should be written.
    """

    return ensure_absolute(
        Path(environ.get("XDG_CACHE_HOME", Path.home().joinpath(".cache"))),
        create=create,
    )
