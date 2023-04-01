"""
Test the 'commands.use' module.
"""

# module under test
from rcmpy import PKG_NAME
from rcmpy.entry import main as rcmpy_main
from rcmpy.paths import override_environ_tempdir


def test_use_command_basic():
    """Test basic usages of the 'use' command."""

    args = [PKG_NAME, "use"]

    # Use a temporary directory for state.
    with override_environ_tempdir("XDG_STATE_HOME"):
        assert rcmpy_main(args) == 0
        assert rcmpy_main(args + ["-d"]) == 0
