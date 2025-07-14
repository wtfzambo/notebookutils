"""
[Preview] notebookutils.udf is a utility to User data functions (UDF).

Below is overview about the available methods:

run(artifactId: String, functionName: String, parameters: Map[String, String] = Map.empty, workspaceId: String = "", capacityId: String = ""): String
-> Run a User data functions (UDF).
getFunctions(udf: String, workspaceId: String = ""): UDF
-> Get the User data functions (UDF).
Use notebookutils.udf.help("methodName") for more info about a method.
"""

from typing import Any


def getFunctions(udf: str, workspaceId: str = "") -> Any:
    """
    [Preview] Get the User data functions (UDF).

    Args:
        udf (str): The UDF artifact id or name.
        workspaceId (str, optional): The UDF workspace id, if not provided, it will be retrieved from the current workspace. Defaults to "".

    Returns:
        UDF: The UDF functions.

    Examples:
        myFunctions = notebookutils.udf.getFunctions("udf01")
        display(myFunctions.functionDetails)  # get function details
        display([myFunctions.itemDetails])  # get item details
        myFunctions.add(1, 2)  # call function add
    """
    pass


def run(
    artifactId: str,
    functionName: str,
    parameters: dict[str, Any] | None = None,
    workspaceId: str = "",
    capacityId: str = "",
) -> str:
    """
    Run a User data functions (UDF).

    Args:
        artifactId (str): The UDF artifact id.
        functionName (str): The UDF function name.
        parameters (dict[str, Any] | None, optional): The UDF parameters. Defaults to None.
        workspaceId (str, optional): The UDF workspace id, if not provided, it will be retrieved from the current workspace. Defaults to "".
        capacityId (str, optional): The UDF capacity id, if not provided, it will be retrieved from the current capacity. Defaults to "".

    Returns:
        str: The UDF execution result.
    """
    return ""


def help(method: str | None = None):
    pass
