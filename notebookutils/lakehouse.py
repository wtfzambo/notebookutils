"""
mssparkutils.lakehouse is a utility to manage Lakehouse artifacts.

Below is overview about the available methods:

create(name: String, description: String = "", definition: ItemDefinition = null, workspaceId: String = ""): Artifact -> Create a new Lakehouse.
get(name: String, workspaceId: String = ""): Artifact -> Get a Lakehouse by name or id.
getWithProperties(name: String, workspaceId: String = ""): Artifact -> Get a Lakehouse with properties by name or id.
update(name: String, newName: String, description: String = "", workspaceId: String = ""): Artifact -> Update a Artifact by name.
delete(name: String, workspaceId: String = ""): Boolean -> Delete a Lakehouse by name.
list(workspaceId: String = "", maxResults: Int = 1000): Array[Artifact] -> List all Lakehouses in the workspace.
listTables(lakehouse: String, workspaceId: String = "", maxResults: Int = 1000): Array[Table] -> List all tables in a Lakehouse artifact.
loadTable(loadOption: collection.Map[String, Any], table: String, lakehouse: String, workspaceId: String = ""): Array[Table] -> # Starts a load table operation in a Lakehouse artifact.

Use mssparkutils.lakehouse.help("methodName") for more info about a method.
"""

from collections.abc import Sequence
from typing import Any


def create(
    name: str, description: str = "", definition: Any = None, workspaceId: str = ""
) -> Any:
    """Create a new Lakehouse.
    Args:
        name (str): Name of the Lakehouse.
        description (str, optional): Description of the Lakehouse. Defaults to "".
        definition (Any, optional): Creation payload for the Lakehouse, Map[String, Any]. Please refer to: https://learn.microsoft.com/en-us/rest/api/fabric/lakehouse/items/create-lakehouse?tabs=HTTP#lakehousecreationpayload. Defaults to None.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.
    """
    pass


def delete(name: str, workspaceId: str = ""):
    pass


def list(workspaceId: str = "", maxResults: int = 1000):
    pass


def get(name: str = "", workspaceId: str = "") -> Any:
    """Get the info of a Lakehouse.

    Args:
        name (str, optional): Name of the Lakehouse. Defaults to "".
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.
    """
    pass


def update(name: str, newName: str, description: str = "", workspaceId: str = ""):
    pass


def getDefinition(name: str, workspaceId: str = ""):
    pass


def updateDefinition(name: str, definition: str, workspaceId: str = ""):
    pass


def listTables(
    lakehouse: str = "", workspaceId: str = "", maxResults: int = 1000
) -> Sequence[Any]:
    """List all tables in a Lakehouse.

    Args:
        lakehouse (str, optional): Name of the Lakehouse, default to default lakehouse. Defaults to "".
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".
        maxResults (int, optional): Maximum number of tables to return, default is 1000. Defaults to 1000.

    Returns:
        Array[Table]: Array of Table objects.
    """
    return []


def loadTable(
    loadOption: dict[str, Any], table: str, lakehouse: str = "", workspaceId: str = ""
) -> bool:
    """Starts a load table operation.

    Args:
        loadOption (dict[str, Any]): Load options. Please refer to https://learn.microsoft.com/en-us/rest/api/fabric/lakehouse/tables/load-table
        table (str): Name of the Table.
        lakehouse (str, optional): Name of the Lakehouse, default to default lakehouse. Defaults to "".
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        bool: Boolean.
    """
    return False


def getWithProperties(name: str, workspaceId: str = "") -> Any:
    """Get the info of a Lakehouse with properties.

    Args:
        name (str): Name of the Lakehouse.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.
    """
    pass


def help(method_name=None):
    pass
