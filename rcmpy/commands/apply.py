"""
An entry-point for the 'apply' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from logging import getLogger

# third-party
from vcorelib.args import CommandFunction as _CommandFunction
from vcorelib.io.types import FileExtension

# internal
from rcmpy import PKG_NAME
from rcmpy.config import Config
from rcmpy.state import load_state

LOG = getLogger(__name__)


def apply_cmd(_: _Namespace) -> int:
    """Execute the apply command."""

    with load_state() as state:
        config_base = state.directory.joinpath(PKG_NAME)

        config_candidates = list(
            FileExtension.data_candidates(config_base, exists_only=True)
        )

        if not config_candidates:
            LOG.error(
                "No config found: %s.",
                list(FileExtension.data_candidates(config_base)),
            )
            return 1

        assert len(config_candidates) == 1, config_candidates

        config = Config.decode(config_candidates[0])
        print(config)

    return 0


def add_apply_cmd(_: _ArgumentParser) -> _CommandFunction:
    """Add apply-command arguments to its parser."""

    return apply_cmd
