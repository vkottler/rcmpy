"""
A module for working with test data.
"""

# built-in
from contextlib import ExitStack, contextmanager
from logging import getLogger
from pathlib import Path
from typing import Iterator

# third-party
from vcorelib.paths import rel
from vcorelib.paths.context import in_dir

# module under test
from rcmpy import PKG_NAME
from rcmpy.entry import main as rcmpy_main
from rcmpy.paths import override_environ_tempdir


def resource(resource_name: str, *parts: str, valid: bool = True) -> Path:
    """Locate the path to a test resource."""

    return Path(__file__).parent.joinpath(
        "data", "valid" if valid else "invalid", resource_name, *parts
    )


LOG = getLogger(__name__)


@contextmanager
def file_removed(path: Path) -> Iterator[None]:
    """
    Remove a file with a managed context (restore the file when complete).
    """

    with path.open("rb") as path_fd:
        contents = path_fd.read()

    path.unlink()
    assert not path.is_file()
    LOG.warning("Removed '%s'.", rel(path))

    try:
        yield
    finally:
        with path.open("wb") as path_fd:
            path_fd.write(contents)
        LOG.warning("Restored '%s'.", rel(path))


@contextmanager
def scenario(name: str, variant: str = None) -> Iterator[Path]:
    """Ensure a specific test scenario is set up for execution."""

    path = resource("scenarios", name)

    with ExitStack() as stack:
        # Use a temporary directory for state and cache.
        for var in ["XDG_STATE_HOME", "XDG_CACHE_HOME"]:
            stack.enter_context(override_environ_tempdir(var))

        # Use the scenario directory as the current directory.
        stack.enter_context(in_dir(path))

        # Updated the config directory to the one for the test scenario.
        assert rcmpy_main([PKG_NAME, "use", str(path)]) == 0

        # Set the variant if it was provided.
        if variant is not None:
            assert rcmpy_main([PKG_NAME, "variant", variant]) == 0

        yield path
