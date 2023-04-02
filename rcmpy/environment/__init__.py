"""
A module implementing the package's runtime environment.
"""

# built-in
from contextlib import contextmanager
from typing import Iterator

# third-party
from vcorelib.paths import Pathlike

# internal
from rcmpy.environment.template import TemplateEnvironment
from rcmpy.state import load_state


class Environment(TemplateEnvironment):
    """A class implementing this package's runtime environment."""


@contextmanager
def load_environment(
    root: Pathlike = None, name: str = "state.json"
) -> Iterator[Environment]:
    """A wrapper for loading an environment with default state data."""

    with load_state(root=root, name=name) as state:
        yield Environment(state)
