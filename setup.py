# =====================================
# generator=datazen
# version=3.1.2
# hash=714a28dd53b72476bfa5eb360f9d801d
# =====================================

"""
rcmpy - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from rcmpy_bootstrap.setup import setup  # type: ignore

# internal
from rcmpy import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Vaughn Kottler",
    "email": "vaughnkottler@gmail.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.10",
        "3.11",
    ],
}
setup(
    pkg_info,
    author_info,
)
