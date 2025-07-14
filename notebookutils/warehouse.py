"""
mssparkutils.warehouse is a utility to manage Warehouse artifacts.

Below is overview about the available methods:

create(name: String, description: String = "", definition: ItemDefinition = null, workspaceId: String = ""): Artifact -> Create a new Warehouse.
get(name: String, workspaceId: String = ""): Artifact -> Get a Artifact by name.
update(name: String, newName: String, description: String = "", workspaceId: String = ""): Artifact -> Update a Warehouse by name.
delete(name: String, workspaceId: String = ""): Boolean -> Delete a Warehouse by name.
list(workspaceId: String = "", maxResults: Int = 1000): Array[Artifact] -> List all Warehouse in the workspace.
getDefinition(name: String, workspaceId: String): ItemDefinition -> Get the definition of a Warehouse.
updateDefinition(name: String, definition: ItemDefinition, workspaceId: String): Boolean -> Update the definition of a Warehouse.

Use mssparkutils.warehouse.help("methodName") for more info about a method.
"""

from typing import Any


def create(
    name: str,
    description: str = "",
    definition: Any = None,
    workspaceId: str = "",
) -> Any:
    """Create a new Warehouse.

    Args:
        name (str): Name of the Warehouse.
        description (str, optional): Description of the Warehouse. Defaults to "".
        definition (Any, optional): Definition of the Warehouse, Map[String, Any]. Please refer to: https://learn.microsoft.com/en-us/rest/api/fabric/core/items/create-item?#itemdefinition. Defaults to None.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.
    """
    pass


def delete(name: str, workspaceId: str = "") -> bool:
    """
    Delete a Warehouse.

    Args:
        name (str): Name of the Warehouse.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        bool: Boolean.
    """
    return False


def list(workspaceId: str = "", maxResults: int = 1000) -> list[Any]:
    """List all Warehouses.

    Args:
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".
        maxResults (int, optional): Maximum number of Warehouses to return, default is 1000. Defaults to 1000.

    Returns:
        list[Artifact]: Array of Artifact objects.
    """
    return []


def get(name: str, workspaceId: str = "") -> Any:
    """Get the info of a Warehouse.

    Args:
        name (str): Name of the Warehouse.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.
    """
    pass


def update(
    name: str, newName: str, description: str = "", workspaceId: str = ""
) -> Any:
    """
    Update the info of a Warehouse.

    Args:
        name (str): Name of the Warehouse.
        newName (str): New name of the Warehouse.
        description (str, optional): New description of the Artifact. Defaults to "".
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.
    """
    pass


def getDefinition(name: str, workspaceId: str = "") -> str:
    """Get the specified Warehouse definition.

    Args:
        name (str): Name of the Warehouse.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        str: string.
    """
    return ""


def updateDefinition(name: str, definition: Any, workspaceId: str = "") -> bool:
    """
    Update the specified Warehouse definition.

    Args:
        name (str): Name of the Warehouse.
        definition (Any): Definition of the Warehouse, please refer to: https://learn.microsoft.com/en-us/rest/api/fabric/core/items/get-item-definition?tabs=HTTP#ItemDefinition
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        bool: true or false.
    """
    return False


def help(method_name: str | None = None):
    pass
