"""
A module for working with test data.
"""

# built-in
from contextlib import ExitStack, contextmanager
from os.path import join
from pathlib import Path
from typing import Iterator

# third-party
import pkg_resources
from vcorelib.paths.context import in_dir

# module under test
from rcmpy import PKG_NAME
from rcmpy.entry import main as rcmpy_main
from rcmpy.paths import override_environ_tempdir


def resource(
    resource_name: str, *parts: str, valid: bool = True, pkg: str = __name__
) -> Path:
    """Locate the path to a test resource."""

    return Path(
        pkg_resources.resource_filename(
            pkg,
            join(
                "data", "valid" if valid else "invalid", resource_name, *parts
            ),
        )
    )


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
