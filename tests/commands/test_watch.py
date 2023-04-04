"""
Test the 'commands.watch' module.
"""

# module under test
from rcmpy import PKG_NAME
from rcmpy.entry import main as rcmpy_main

# internal
from tests.resources import scenario


def test_watch_command_basic():
    """Test basic usages of the 'watch' command."""

    args = [PKG_NAME, "watch"]

    with scenario("simple"):
        assert rcmpy_main(args + ["-i", ".", "--", "python", "--version"]) == 0
