"""
A module implementing a configuration interface for the package.
"""

# built-in
from typing import Any, Dict, List, Set

# third-party
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec
from vcorelib.io.types import JsonObject as _JsonObject

# internal
from rcmpy.schemas import RcmpyDictCodec as _RcmpyDictCodec

FilesConfig = List[Dict[str, Any]]


class Config(_RcmpyDictCodec, _BasicDictCodec):
    """The top-level configuration object for the package."""

    def init(self, data: _JsonObject) -> None:
        """Initialize this instance."""
        self.data = data

        self.files: FilesConfig = data.get("files", [])  # type: ignore

        # A set of templates that are used by this config.
        self.templates: Set[str] = {x["template"] for x in self.files}

    def asdict(self) -> _JsonObject:
        """Obtain a dictionary representing this instance."""
        return self.data
