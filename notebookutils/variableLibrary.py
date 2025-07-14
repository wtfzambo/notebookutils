"""
 [Preview] notebookutils.variableLibrary is a utility to Variable Library.

Below is overview about the available methods:

get(variableReference: String): String
-> Run the variable value with type.
getLibrary(variableLibraryName: String): VariableLibrary
-> Get the variable library.
Use notebookutils.variableLibrary.help("methodName") for more info about a method.
"""

from typing import Any


def get(variableReference: str) -> str:
    """Resolve the variable library reference.

    This method supports the variable library in the same workspace currently.
    It cannot be used with child notebooks to get variable library across workspaces in reference run.

    Args:
        variableReference (str): The Variable Library reference.

    Returns:
        str: The variable value with type.

    Examples:
        >>> notebookutils.variableLibrary.get("$(/**/vl01/test_int)")
        123
        >>> notebookutils.variableLibrary.get("$(/**/vl01/test_string)")
        "test"
        >>> notebookutils.variableLibrary.get("$(/**/vl01/test_bool)")
        True
        >>> notebookutils.variableLibrary.get("$(/**/vl01/test_date)")
        "2025-01-14T16:15:20.123Z"
    """
    return ""


def getLibrary(variableLibraryName: str) -> Any:
    """Get the variable library.

    This method supports the variable library in the same workspace currently.
    It cannot be used with child notebooks to get variable library across workspaces in reference run.

    Args:
        variableLibraryName (str): The Variable Library name.

    Returns:
        Any: The variable library object.

    Examples:
        >>> notebookutils.variableLibrary.getLibrary("vl01").test_int
        123
        >>> notebookutils.variableLibrary.getLibrary("vl01").test_string
        "test"
    """
    pass


def help(method: str | None = None):
    pass
