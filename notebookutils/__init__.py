"""
This module provides various utilities for users to interact with the rest of Synapse notebook.
fs: Utility for filesystem operations in Synapse
notebook: Utility for notebook operations (e.g, chaining Synapse notebooks together)
credentials: Utility for obtaining credentials (tokens and keys) for Synapse resources
env: Utility for obtaining environment metadata (e.g, userName, clusterId etc)
[Learn more](https://go.microsoft.com/fwlink/?linkid=2152237)
"""

__version__ = "1.1.11"  # match Synapse / Fabric notebookutils version number.

__all__ = [
    "data",
    "fs",
    "lakehouse",
    "notebook",
    "session",
    "runtime",
    "fabricClient",
    "credentials",
    "udf",
]

from . import (
    credentials,
    data,
    fabricClient,
    fs,
    lakehouse,
    notebook,
    runtime,
    session,
    udf,
)


def help(module_name=""):
    pass


def __getattr__(name):
    pass
