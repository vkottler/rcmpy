"""
Test the 'commands.apply' module.
"""

# module under test
from rcmpy import PKG_NAME
from rcmpy.entry import main as rcmpy_main

# internal
from tests.resources import scenario


def test_apply_command_empty():
    """Test the 'apply' command against the 'empty' scenario."""

    with scenario("empty"):
        assert rcmpy_main([PKG_NAME, "apply"]) != 0


def test_apply_command_simple():
    """Test the 'apply' command against the 'simple' scenario."""

    with scenario("simple", variant="test"):
        assert rcmpy_main([PKG_NAME, "apply"]) == 0


def test_apply_command_missing_template():
    """Test the 'apply' command against the 'missing_template' scenario."""

    with scenario("missing_template"):
        assert rcmpy_main([PKG_NAME, "apply"]) != 0
