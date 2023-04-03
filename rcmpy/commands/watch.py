"""
An entry-point for the 'watch' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from asyncio import Event, get_event_loop, sleep
from logging import getLogger
from os import getpid
from pathlib import Path

# third-party
from vcorelib.args import CommandFunction as _CommandFunction
from vcorelib.asyncio import run_handle_stop
from vcorelib.paths.info_cache import FileChanged, file_info_cache

# internal
from rcmpy.paths import default_cache_directory

LOG = getLogger(__name__)


def watch_cache() -> Path:
    """Obtain a file path to use as a cache."""
    return default_cache_directory().joinpath(f"watch_cache-{getpid()}.json")


async def entry(stop_sig: Event, args: _Namespace) -> int:
    """TODO."""

    cache_file = watch_cache()

    count = 0

    def poll_cb(_: FileChanged) -> bool:
        """Method to run when any watched file changes."""

        nonlocal count
        count += 1
        return True

    with file_info_cache(cache_file, poll_cb, logger=LOG) as files:
        while not stop_sig.is_set():
            files.poll_directory(args.directory, base=args.dir)
            files.poll_existing(base=args.dir)

            if count > 0:
                # Run the command, return True if it exits 0.
                print(args.cmd)
                count = 0

            if args.single_pass:
                stop_sig.set()

            # Would be neat to implement something to keep this going at
            # a regular period
            await sleep(args.poll_rate)

    # The cache file shouldn't persist across invocations.
    cache_file.unlink()
    return 0


def watch_cmd(args: _Namespace) -> int:
    """Execute the watch command."""

    eloop = get_event_loop()
    stop_sig = Event()
    return run_handle_stop(stop_sig, entry(stop_sig, args), eloop=eloop)


def add_watch_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add watch-command arguments to its parser."""

    parser.add_argument(
        "-p",
        "--poll-rate",
        type=float,
        default=0.1,
        help="poll period in seconds (default: %(default)ss)",
    )
    parser.add_argument(
        "-s",
        "--single-pass",
        action="store_true",
        help="only run a single iteration",
    )
    parser.add_argument(
        "directory", type=Path, help="directory to watch for file changes"
    )
    parser.add_argument("cmd", nargs="+", help="command to run")

    return watch_cmd
