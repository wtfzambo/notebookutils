from warnings import deprecated

__DEPRECATED_MSG = """The namespace mssparkutils is deprecated, please use notebookutils.notebook instead."""


@deprecated(__DEPRECATED_MSG)
def updateNBSEndpoint(endpoint):
    pass


@deprecated(__DEPRECATED_MSG)
def help(method_name=None):
    pass


@deprecated(__DEPRECATED_MSG)
def run(path, timeout_seconds=90, arguments={}, workspace=""):
    return ""


@deprecated(__DEPRECATED_MSG)
def exit(value):
    pass


@deprecated(__DEPRECATED_MSG)
def runMultiple(dag, config=None):
    pass


@deprecated(__DEPRECATED_MSG)
def validateDAG(dag):
    pass
