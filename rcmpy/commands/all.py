# =====================================
# generator=datazen
# version=3.1.2
# hash=e990bc9fe3294af3d40349e7b0627ad4
# =====================================

"""
A module aggregating package commands.
"""

# built-in
from typing import List as _List
from typing import Tuple as _Tuple

# third-party
from vcorelib.args import CommandRegister as _CommandRegister

# internal
from rcmpy.commands.apply import add_apply_cmd
from rcmpy.commands.use import add_use_cmd
from rcmpy.commands.variant import add_variant_cmd
from rcmpy.commands.watch import add_watch_cmd


def commands() -> _List[_Tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "apply",
            "apply any pending changes from the active data repository",
            add_apply_cmd,
        ),
        (
            "use",
            "set the directory to use as the rcmpy data repository",
            add_use_cmd,
        ),
        (
            "variant",
            "set the variant of configuration data to use",
            add_variant_cmd,
        ),
        (
            "watch",
            "do a task whenever a file in a specified directory changes",
            add_watch_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
