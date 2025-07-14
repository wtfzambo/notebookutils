from warnings import deprecated

__DEPRECATED_MSG = """The namespace mssparkutils is deprecated, please use notebookutils.session instead."""


@deprecated(__DEPRECATED_MSG)
def stop():
    pass


@deprecated(__DEPRECATED_MSG)
def restartPython():
    pass
