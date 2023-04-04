"""
A module for working with test data.
"""

# built-in
from contextlib import contextmanager
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

    # Use a temporary directory for state.
    with override_environ_tempdir("XDG_STATE_HOME"):
        with in_dir(path):
            assert rcmpy_main([PKG_NAME, "use", str(path)]) == 0

            # Set the variant if it was provided.
            if variant is not None:
                assert rcmpy_main([PKG_NAME, "variant", variant]) == 0

            yield path
