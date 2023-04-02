"""
A module implementing the package's runtime environment.
"""

# built-in
from contextlib import contextmanager
from typing import Iterator, Optional

# third-party
from vcorelib.io.types import FileExtension
from vcorelib.logging import LoggerMixin
from vcorelib.paths import Pathlike

# internal
from rcmpy import PKG_NAME
from rcmpy.config import Config
from rcmpy.state import State, load_state


class Environment(LoggerMixin):
    """A class implementing this package's runtime environment."""

    def __init__(self, state: State) -> None:
        """Initialize this instance."""

        super().__init__()
        self.state = state
        self._config: Optional[Config] = None

        config_base = state.directory.joinpath(PKG_NAME)

        config_candidates = list(
            FileExtension.data_candidates(config_base, exists_only=True)
        )

        if not config_candidates:
            self.logger.error(
                "No config found: %s.",
                list(FileExtension.data_candidates(config_base)),
            )
        else:
            assert len(config_candidates) == 1, config_candidates
            self._config = Config.decode(config_candidates[0])
            self.logger.info("Loaded config '%s'.", config_candidates[0])

    @property
    def config_loaded(self) -> bool:
        """Determine if this environment has loaded a config."""
        return self._config is not None

    @property
    def config(self) -> Config:
        """Get this environment's configuration object."""
        assert self._config is not None, "Config not loaded!"
        return self._config


@contextmanager
def load_environment(
    root: Pathlike = None, name: str = "state.json"
) -> Iterator[Environment]:
    """A wrapper for loading an environment with default state data."""

    with load_state(root=root, name=name) as state:
        yield Environment(state)
