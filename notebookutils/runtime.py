"""
mssparkutils.runtime utility supports you get context information of runtime that matters to current session.

Below are the available methods in Notebook runtime utility:

notebookutils.runtime.context: Map[String, Any] -> Get the current runtime context.
notebookutils.runtime.help("methodName"): Show more details of a specific method.
"""

context = {}


def getCurrentWorkspaceId():
    pass


def help(method_name: str | None = None):
    pass
