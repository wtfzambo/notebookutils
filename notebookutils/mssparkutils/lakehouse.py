from warnings import deprecated

__DEPRECATED_MSG = """The namespace mssparkutils is deprecated, please use notebookutils.lakehouse instead."""


@deprecated(__DEPRECATED_MSG)
def create(name, description="", definition=None, workspaceId=""):
    pass


@deprecated(__DEPRECATED_MSG)
def delete(name, workspaceId=""):
    pass


@deprecated(__DEPRECATED_MSG)
def list(workspaceId="", maxResults=1000):
    pass


@deprecated(__DEPRECATED_MSG)
def get(name, workspaceId=""):
    pass


@deprecated(__DEPRECATED_MSG)
def update(name, newName, description="", workspaceId=""):
    pass


@deprecated(__DEPRECATED_MSG)
def help(method_name=None):
    pass
