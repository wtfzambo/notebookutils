"""
This module provides various utilities for users to interact with the rest of Synapse notebook.
fs: Utility for filesystem operations in Synapse
notebook: Utility for notebook operations (e.g, chaining Synapse notebooks together)
credentials: Utility for obtaining credentials (tokens and keys) for Synapse resources

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
    "credentials",
    "udf",
    "session",
    "variableLibrary",
    "warehouse",
    "workspace",
]

from . import (
    credentials,
    data,
    fs,
    lakehouse,
    notebook,
    runtime,
    session,
    udf,
    variableLibrary,
    warehouse,
    workspace,
)


def help(module_name=""):
    pass


def __getattr__(name):
    pass
