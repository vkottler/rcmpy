"""
Test the 'commands.apply' module.
"""

# module under test
from rcmpy import PKG_NAME
from rcmpy.entry import main as rcmpy_main

# internal
from tests.resources import file_removed, scenario


def test_apply_command_empty():
    """Test the 'apply' command against the 'empty' scenario."""

    with scenario("empty"):
        assert rcmpy_main([PKG_NAME, "apply"]) != 0


def test_apply_command_simple():
    """Test the 'apply' command against the 'simple' scenario."""

    with scenario("simple", variant="test") as root:
        assert rcmpy_main([PKG_NAME, "apply"]) == 0

        templates = root.joinpath("templates")

        # Remove the 'test.txt' template in the variant directory
        # (temporarily).
        with file_removed(templates.joinpath("test", "test.txt")):
            assert rcmpy_main([PKG_NAME, "apply"]) == 0

            # Remove the 'test.txt' template in the common directory
            # (temporarily).
            with file_removed(templates.joinpath("common", "test.txt")):
                assert rcmpy_main([PKG_NAME, "apply"]) != 0

            # Run again with the common template restored.
            assert rcmpy_main([PKG_NAME, "apply"]) == 0

        # Run again with the variant template restored.
        assert rcmpy_main([PKG_NAME, "apply"]) == 0


def test_apply_command_missing_template():
    """Test the 'apply' command against the 'missing_template' scenario."""

    with scenario("missing_template"):
        assert rcmpy_main([PKG_NAME, "apply"]) != 0
