"""
mssparkutils.workspace is a utility to manage workspace.

Below is overview about the available methods:

assignToCapacity(capacityId: String, workspaceId: String = ""): Boolean -> Assigns the specified workspace to the specified capacity.
create(name: String, description: String = "", capacityId: String = ""): Workspace -> Create a new Workspace.
delete(workspaceId: String): Boolean -> Delete a Workspace.
get(name: String = ""): Workspace -> Get the info of a Workspace.
list(maxResults: Int = 1000): Array[Workspace] -> Returns a list of workspaces the user has access to.
unassignFromCapacity(workspaceId: String): Boolean -> Unassigns the specified workspace to the specified capacity.
update(workspaceId: String, newName: String, description: String = ""): Workspace -> Update the info of a Workspace.

Use mssparkutils.workspace.help("methodName") for more info about a method.
"""

from typing import Any, Sequence


def assignToCapacity(capacityId: str, workspaceId: str = "") -> bool:
    """Assigns the specified workspace to the specified capacity.

    Args:
        capacityId (str): Id of the capacity.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        bool: Boolean.
    """
    return False


def unassignFromCapacity(workspaceId: str) -> bool:
    """Unassigns the specified workspace to the specified capacity.

    Args:
        workspaceId (str): Id of the workspace.

    Returns:
        bool: Boolean.
    """
    return False


def create(name: str, description: str = "", capacityId: str = "") -> Any:
    """Create a new Workspace.
    Args:
        name (str): Name of the Workspace.
        description (str, optional): Description of the Workspace. Defaults to "".
        capacityId (str, optional): Id of the capacity, default to current capacity. Defaults to "".

    Returns:
        Workspace: Workspace object.
    """
    pass


def delete(workspaceId: str) -> bool:
    """
    Delete a Workspace.
    Args:
        workspaceId (str): Id of the workspace.

    Returns:
        bool: Boolean.
    """
    return False


def list(maxResults: int = 1000) -> list[Any]:
    """List all workspaces the user has access to.

    Args:
        maxResults (int, optional): Maximum number of workspaces to return. Defaults to 1000.

    Returns:
        list[Workspace]: Array of Workspace objects.
    """
    return []


def get(name: str = "") -> Any:
    """Get the info of a Workspace.

    Args:
        name (str, optional): Name or Id of the Workspace. Defaults to current workspace.

    Returns:
        Workspace: Workspace object.
    """
    pass


def update(workspaceId: str, newName: str, description: str = "") -> Any:
    """
    Update the info of a Workspace.

    Args:
        workspaceId (str): Id of the workspace.
        newName (str): New name of the Workspace.
        description (str, optional): New description of the Workspace. Defaults to "".

    Returns:
        Workspace: Workspace object.
    """
    pass


def listArtifacts(
    artifactType: str, workspaceId: str = "", maxResults: int = 1000
) -> Sequence[Any]:
    """List the specified type of artifacts.

    Args:
        artifactType (str): Type of the artifact.
        workspaceId (str, optional): Id of the workspace. Defaults to "".
        maxResults (int, optional): Maximum number of artifacts to return. Defaults to 1000.

    Returns:
        Sequence[Artifact]: Array of Artifact objects.
    """
    return []


def help(method_name: str | None = None):
    pass
