"""
Test the 'commands.apply' module.
"""

# module under test
from rcmpy import PKG_NAME
from rcmpy.entry import main as rcmpy_main

# internal
from tests.resources import scenario


def test_apply_command_basic():
    """Test basic usages of the 'apply' command."""

    args = [PKG_NAME, "apply"]

    with scenario("empty"):
        assert rcmpy_main(args) != 0

    with scenario("simple"):
        assert rcmpy_main(args) == 0
