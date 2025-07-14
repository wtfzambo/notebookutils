"""
The notebook module.

exit(value: String): void -> This method lets you exit a notebook with a value.
run(path: String, timeoutSeconds: int, arguments: Map, workspace: String): String -> This method runs a notebook and returns its exit value.
runMultiple(DAG: Any): Map[String, MsNotebookRunResult] -> [Preview] Runs multiple notebooks concurrently with support for dependency relationships.
validateDAG(DAG: Any): Boolean -> [Preview] This method check if the DAG is correctly defined.

[Preview] Below methods are only support Fabric Notebook.
create(name: String, description: String = "", content: String = "", defaultLakehouse: String = "", defaultLakehouseWorkspace: String = "", workspaceId: String = ""): Artifact -> Create a new Notebook.
get(name: String, workspaceId: String = ""): Artifact -> Get a Notebook by name or id.
update(name: String, newName: String, description: String = "", workspaceId: String = ""): Artifact -> Update a Artifact by name.
delete(name: String, workspaceId: String = ""): Boolean -> Delete a Notebook by name.
list(workspaceId: String = "", maxResults: Int = 1000): Array[Artifact] -> List all Notebooks in the workspace.
updateDefinition(name: String, content: String = "", defaultLakehouse: String = "", defaultLakehouseWorkspace: String = "", workspaceId: String = "") -> Update the definition of a Notebook.

Use notebookutils.notebook.help("methodName") for more info about a method.
"""

from typing import Any


def updateNBSEndpoint(endpoint):
    pass


def help(method_name: str | None = None):
    pass


def run(
    path: str,
    timeout_seconds: int = 90,
    arguments: dict[str, Any] = {},
    workspaceId: str = "",
) -> str:
    """This method runs a notebook and returns its exit value.

    The notebook will run in the current livy session context by default.
    Args:
        path (str): absolute path to the notebook, e.g. /path/to/notebook
        timeout_seconds (int, optional): timeout in seconds for the called notebook. If the run failed
            to finish within this time, this method will throw an exception. Defaults to 90.
        arguments (dict[str, Any], optional): string map of arguments to pass to the notebook. Defaults to {}.
        workspaceId (str, optional): the workspace to run the notebook in, support workspace name or workspace id.
            If not specified, use current workspace. Defaults to "".

    Returns:
        str: the string returned by msutils.notebook.exit() or null

    Raises:
        NotebookExecutionException: if the notebook run did not complete successfully
    """
    return ""


def exit(value: str):
    """This method lets you exit a notebook with a value.

    Args:
        value (str): the value to return when exiting
    """
    pass


def runMultiple(
    dag: Any,  # pyright: ignore[reportAny]
    config: dict[str, Any] | None = None,
) -> dict[str, dict[str, Any]]:
    """Runs multiple notebooks concurrently with support for dependency relationships.

    Args:
        dag (Any): A list of notebook names or a complex data structure (dict or JSON string)
            that meets the requirements of the com.microsoft.spark.notebook.msutils.impl.MsNotebookPipeline scala class.
            You can use @activity('your activity name').exitValue() in args to get the exit value of the dependency activity.
        config (dict[str, Any], optional): Configuration for the display DAG graph, only supported in python.
            Keys include: displayDAGViaGraphviz, showArgs, showTime
            for example: `{"displayDAGViaGraphviz": True}`
            displayDAGViaGraphviz: whether to display DAG graph via graphviz, default to False
            showArgs: whether to show args in DAG graph, default to False
            showTime: whether to show time in DAG graph, default to False
            Defaults to None.

    Returns:
        dict[str, dict[str, Any]]: key is activity name, value is a MsNotebookRunResult, which contains the following attributes: exitVal, exception

    Note:
        1. The recommended number and concurrency of notebooks to run should not exceed 50.
        Having more than 50 notebook activities or exceeding the concurrency limit
        may have stability and performance issues due to compute resource usage.
        If issues happens, consider separating notebooks into multiple runMultiple calls,
        or reducing the number of concurrency by change the "concurrency" field of the DAG parameter.
        More details please refer to https://aka.ms/fabric/notebookutils#reference-run-multiple-notebooks-in-parallel

    Examples:
        Run multiple notebooks by providing a list of notebook names:
        >>> mssparkutils.notebook.runMultiple(["notebook1", "notebook2", "notebook3"])

        Run multiple notebooks by providing a complex data structure (dict or JSON string):
        >>> DAG = {
        ...     "activities": [
        ...         {
        ...             "name": "notebook1",  # activity name, must be unique
        ...             "path": "notebook1",  # notebook path
        ...             "timeoutPerCellInSeconds": 90,  # max timeout for each cell, default to 90 seconds
        ...             "args": {"param1": "value1"},  # notebook parameters
        ...             "workspace": "workspace1",  # workspace name, default to current workspace
        ...             "retry": 0,  # max retry times, default to 0
        ...             "retryIntervalInSeconds": 0,  # retry interval, default to 0 seconds
        ...             "dependencies": []  # list of activity names that this activity depends on
        ...         },
        ...         {
        ...             "name": "notebook2",
        ...             "path": "notebook2",
        ...             "timeoutPerCellInSeconds": 120,
        ...             "args": {
        ...                 "useRootDefaultLakehouse": True,  # set useRootDefaultLakehouse as True to ignore that child notebook attach a different default lakehouse
        ...                 "param1": "@activity('notebook1').exitValue()"  # use exit value of notebook1
        ...             },
        ...             "retry": 1,
        ...             "retryIntervalInSeconds": 10,
        ...             "dependencies": ["notebook1"]
        ...         }
        ...     ],
        ...     "timeoutInSeconds": 43200,  # max timeout for the entire pipeline, default to 12 hours
        ...     "concurrency": 50,  # max number of notebooks to run concurrently, default to 50, 0 means unlimited
        ...     "refreshInterval": 3  # interval to refresh the status of the pipeline, default to 3 seconds
        ... }
        >>> mssparkutils.notebook.runMultiple(DAG)
    """
    return {}


def validateDAG(dag: Any) -> bool:  # pyright: ignore[reportAny]
    """Check if the DAG is correctly defined, if the syntax is correct, and if notebooks are found in the workspace without actual execution, etc.

    Args:
        dag (Any): A list of notebook names or a complex data structure (dict or JSON string)
            that meets the requirements of the com.microsoft.spark.notebook.msutils.impl.MsNotebookPipeline scala class.

    Returns:
        bool: True if the DAG is correctly defined, False otherwise.
    """
    return False


def create(
    name: str,
    description: str = "",
    content: str | None = None,
    defaultLakehouse: str = "",
    defaultLakehouseWorkspace: str = "",
    workspaceId: str = "",
) -> Any:
    """Create a new Notebook.

    Args:
        name (str): Name of the Notebook.
        description (str, optional): Description of the Notebook. Defaults to "".
        content (str | None, optional): Content of the Notebook, ipynb json format. Defaults to None.
        defaultLakehouse (str, optional): Default lakehouse of the Notebook. Defaults to "".
        defaultLakehouseWorkspace (str, optional): Default lakehouse workspace of the Notebook. Defaults to "".
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.

    Examples:
        Read notebook content from file and create notebook:
        >>> with open("/path/to/notebook.ipynb", "r") as f:
        ...     content = f.read()
        >>> mssparkutils.notebook.create("notebook1", "notebook1 description", content, "lakehouse1", "workspace1")
    """
    pass


def delete(name: str, workspaceId: str = "") -> bool:
    """
    Delete a notebook

    Args:
        name (str): Name of the Notebook.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        bool: Boolean.
    """
    return False


def list(workspaceId: str = "", maxResults: int = 1000) -> list[Any]:
    """List all Notebooks.

    Args:
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".
        maxResults (int, optional): Maximum number of Notebooks to return, default is 1000. Defaults to 1000.

    Returns:
        Array[Artifact]: Array of Artifact objects.
    """
    return []


def get(name: str, workspaceId: str = "") -> Any:
    """Get the info of a Notebook.

    Args:
        name (str): Name of the Notebook.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.
    """
    pass


def update(
    name: str, newName: str, description: str = "", workspaceId: str = ""
) -> Any:
    """
    Update the info of a Notebook.

    Args:
        name (str): Name of the Notebook.
        newName (str): New name of the Notebook.
        description (str, optional): New description of the Artifact. Defaults to "".
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".

    Returns:
        Artifact: Artifact object.
    """
    pass


def updateDefinition(
    name: str,
    content: str | None = None,
    defaultLakehouse: str = "",
    defaultLakehouseWorkspace: str = "",
    workspaceId: str = "",
    environmentId: str = "",
    environmentWorkspaceId: str = "",
) -> bool:
    """
    Update the definition of a Notebook.

    Args:
        name (str): Name of the Notebook.
        content (str | None, optional): Content of the Notebook, json format. If empty, keep the original content. Defaults to None.
        defaultLakehouse (str, optional): Default lakehouse of the Notebook. Defaults to "".
        defaultLakehouseWorkspace (str, optional): Default lakehouse workspace of the Notebook. Defaults to "".
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".
        environmentId (str, optional): Id of the environment. Defaults to "".
        environmentWorkspaceId (str, optional): Id of the environment workspace, default to current workspace. Defaults to "".

    Returns:
        bool: true or false.
    """
    return False


def getDefinition(name: str, workspaceId: str = "", format: str = "ipynb") -> str:
    """Get the definition of a Notebook.

    Args:
        name (str): Name of the Notebook.
        workspaceId (str, optional): Id of the workspace, default to current workspace. Defaults to "".
        format (str, optional): Format of the notebook, default to ipynb. Defaults to "ipynb".

    Returns:
        str: content string of notebook.
    """
    return ""
