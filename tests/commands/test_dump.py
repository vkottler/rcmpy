"""
Test the 'commands.dump' module.
"""

# module under test
from rcmpy import PKG_NAME
from rcmpy.entry import main as rcmpy_main

# internal
from tests.resources import scenario


def test_dump_command_empty():
    """Test the 'apply' command against the 'empty' scenario."""

    with scenario("simple", variant="test") as _:
        assert rcmpy_main([PKG_NAME, "dump"]) == 0
