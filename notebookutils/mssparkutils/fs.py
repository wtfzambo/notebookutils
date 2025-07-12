from warnings import deprecated

__DEPRECATED_MSG = (
    """The namespace mssparkutils is deprecated, please use notebookutils.fs instead."""
)


@deprecated(__DEPRECATED_MSG)
def help(method_name=None):
    pass


@deprecated(__DEPRECATED_MSG)
def cp(src, dest, recurse=False):
    return False


@deprecated(__DEPRECATED_MSG)
def mv(src, dest, create_path=False, overwrite=False):
    return False


@deprecated(__DEPRECATED_MSG)
def ls(dir):
    return []


@deprecated(__DEPRECATED_MSG)
def mkdirs(dir):
    return False


@deprecated(__DEPRECATED_MSG)
def put(file, content, overwrite=False):
    return False


@deprecated(__DEPRECATED_MSG)
def head(file, max_bytes=1024 * 100):
    return False


@deprecated(__DEPRECATED_MSG)
def append(file, content, createFileIfNotExists=False):
    return False


@deprecated(__DEPRECATED_MSG)
def rm(dir, recurse=False):
    return False


@deprecated(__DEPRECATED_MSG)
def exists(file):
    return False


@deprecated(__DEPRECATED_MSG)
def mountToDriverNode(source, mountPoint, extraConfigs={}):
    return False


@deprecated(__DEPRECATED_MSG)
def unmountFromDriverNode(mountPoint):
    return False


@deprecated(__DEPRECATED_MSG)
def mount(source, mountPoint, extraConfigs={}):
    return False


@deprecated(__DEPRECATED_MSG)
def unmount(mountPoint, extraOptions={}):
    return False


@deprecated(__DEPRECATED_MSG)
def mounts(extraOptions={}):
    return False


@deprecated(__DEPRECATED_MSG)
def refreshMounts():
    return False


@deprecated(__DEPRECATED_MSG)
def getMountPath(mountPoint, scope=""):
    return False


@deprecated(__DEPRECATED_MSG)
def fastcp(src, dest, recurse=True, extraConfigs={}):
    return False
