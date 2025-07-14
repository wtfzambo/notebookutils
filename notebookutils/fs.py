"""
mssparkutils.fs provides utilities for working with various FileSystems.

Below is overview about the available methods:

cp(from: String, to: String, recurse: Boolean = false): Boolean -> Copies a file or directory, possibly across FileSystems
fastcp(from: String, to: String, recurse: Boolean = true): Boolean -> Copies a file or directory via azcopy, possibly across FileSystems.
mv(from: String, to: String, createPath: Boolean = false, overwrite: Boolean = false): Boolean -> Moves a file or directory, possibly across FileSystems
ls(dir: String): Array -> Lists the contents of a directory
mkdirs(dir: String): Boolean -> Creates the given directory if it does not exist, also creating any necessary parent directories
put(file: String, contents: String, overwrite: Boolean = false): Boolean -> Writes the given String out to a file, encoded in UTF-8
head(file: String, maxBytes: int = 1024 * 100): String -> Returns up to the first 'maxBytes' bytes of the given file as a String encoded in UTF-8
append(file: String, content: String, createFileIfNotExists: Boolean): Boolean -> Append the content to a file
rm(dir: String, recurse: Boolean = false): Boolean -> Removes a file or directory
exists(file: String): Boolean -> Check if a file or directory exists
mount(source: String, mountPoint: String, extraConfigs: Map[String, Any]): Boolean -> Mounts the given remote storage directory at the given mount point
unmount(mountPoint: String): Boolean -> Deletes a mount point
mounts(): Array[MountPointInfo] -> Show information about what is mounted
getMountPath(mountPoint: String, scope: String = ""): String -> Gets the local path of the mount point

Use mssparkutils.fs.help("methodName") for more info about a method.
"""

from typing import Any


def help(method_name: str | None = None):
    pass


def cp(src: str, dest: str, recurse: bool = False) -> bool:
    """Copies a file or directory, possibly across FileSystems.

    Example: `cp("/tmp/my-folder/a", "adls://xxx/tmp/b")`.

    Args:
        src (str): FileSystem URI of the source file or directory.
        dest (str): FileSystem URI of the destination file or directory.
        recurse (bool, optional): If True, all files and directories
            will be recursively copied. Defaults to False.

    Returns:
        bool: True if all files were successfully copied.
    """
    return False


def mv(src: str, dest: str, create_path: bool = False, overwrite: bool = False) -> bool:
    """Moves a file or directory, possibly across FileSystems.

    For intra-FileSystem, it is implemented by hadoop fs rename operation.
    For inter-FileSystem, This is implemented as a copy followed by delete.

    Example: `mv("/tmp/my-folder/", "adls:/xxx/tmp/b")`.

    Args:
        src (str): FileSystem URI of the source file or directory.
        dest (str): FileSystem URI of the destination file or directory.
        create_path (bool, optional): If True, will firstly create the parent dir
            if not exists before move op. Defaults to False.
        overwrite (bool, optional): If True, will overwrite the destination folder
            if exists. Defaults to False.
    Returns:
        bool: True if the move was successful (so 'src' is deleted and 'dest' contains the data).
    """
    return False


def ls(dir: str) -> list:  # pyright: ignore[reportMissingTypeArgument]
    """Lists the contents of a directory.

    Example: `ls("/tmp/my-folder/")`.

    The MSFileInfo object that is returned has the following useful info::

        files = mssparkutils.fs.ls("/mnt/my-folder/")
        file = files[0]
        f.name  # myFile
        f.size  # 1286
        f.path  # "/mnt/my-folder/myFile"
        f.isDir  # false
        f.isFile  # true
        f.modifyTime  # 1586829450000

    Args:
        dir (str): FileSystem URI

    Returns:
        list: List of MSFileInfos containing the name and size of each file.
    """
    return []


def mkdirs(dir: str) -> bool:
    """Creates the given directory if it does not exist, also creating any necessary parent directories.

    Example: `mkdirs("/tmp/a/b/c")`.

    Args:
        dir (str): FileSystem URI

    Returns:
        bool: True if the directory was successfully created.
    """
    return False


def put(file: str, content: str, overwrite: bool = False) -> bool:
    """Writes the given String out to a file, encoded in UTF-8.

    Example: `put("/tmp/my-file", "Hello world!", True)`.

    Args:
        file (str): FileSystem URI.
        content (str): Content of file to write, encoded in System default charset.
        overwrite (bool, optional): If set to true, the file will be overwritten if it existed already.
            Note that if overwrite is true and the the write fails, the original file
            may still be deleted. Defaults to False.

    Returns:
        bool: True if the file was successfully written.
    """
    return False


def head(file: str, max_bytes: int = 1024 * 100) -> str:
    """Returns up to the first 'maxBytes' bytes of the given file as a String encoded in UTF-8.

    Example: `head("/tmp/my-folder/my-file")`.

    Args:
        file (str): FileSystem URI.
        max_bytes (int, optional): Maximum number of bytes to read. Defaults to 1024*100.

    Returns:
        str: String containing contents of the file, possibly truncated to the max bytes.
    """
    return ""


def append(file: str, content: str, createFileIfNotExists: bool = False) -> bool:
    """Append the given String to a file, encoded in UTF-8.

    Example: `append("/tmp/my-file", "Hello world!", True)`.

    Args:
        file (str): FileSystem URI.
        content (str): Content needs to be append to file, encoded in System default charset.
        createFileIfNotExists (bool, optional): If set to true, will firstly try to create file if not exists. Defaults to False.

    Returns:
        bool: True if the content was successfully appended to the file.
    """
    return False


def rm(dir: str, recurse: bool = False) -> bool:
    """Removes a file or directory.

    Example: `rm("/tmp/my-folder/", true)`.

    Args:
        dir (str): FileSystem URI for a single file or a directory.
        recurse (bool, optional): If true, all files and directories will be recursively deleted. Defaults to False.

    Returns:
        bool: True if the file or directory was present and is now deleted.
    """
    return False


def exists(file: str) -> bool:
    """Check if a file or directory exists.

    Example: `exists("/tmp/my-file")`.
    Args:
        file (str): FileSystem URI for a single file or a directory.
    Returns:
        bool: True if the file or directory exists.
    """
    return False


def mountToDriverNode(source, mountPoint, extraConfigs={}):
    return False


def unmountFromDriverNode(mountPoint):
    return False


def mount(source: str, mountPoint: str, extraConfigs: dict[str, Any] = {}) -> bool:
    """Mounts the given remote storage directory at the given mount point.

    Examples::

        mount("abfss://CONTAINER@ACCOUNT.dfs.core.windows.net", "/mnt", {"accountKey": "****"})
        mount("abfss://CONTAINER@ACCOUNT.dfs.core.windows.net", "/mnt", {"sasToken": "****"})
        ls(getMountPath("/mnt"))

    It is recommended to always use getMountPath() to obtain the local path of mount point.

    Args:
        source (str): FileSystem URI that contains the source data.
        mountPoint (str): The directory to mount the source. This must start with /.
        extraConfigs (dict[str, Any], optional): A map containing extra configurations.
            Please only provide configs that are advised by Azure documentations. Defaults to {}.

    Returns:
        bool: True if the path was successfully mounted.
    """
    return False


def unmount(mountPoint: str, extraOptions: dict[str, Any] = {}) -> bool:
    """Deletes a mount point.

    Example: `unmount("/mnt")`.

    Args:
        mountPoint (str): Directory previously mounted.
        extraOptions (dict[str, Any], optional): Additional options for unmounting. Defaults to {}.

    Returns:
        bool: True if the mount point was successfully unmounted, or wasn't mounted originally.
    """
    return False


def mounts(extraOptions: dict[str, Any] = {}) -> list:  # pyright: ignore[reportMissingTypeArgument]
    """Show information about what is mounted.

    Any credentials used to mount the mount points listed will not be displayed.

    Example: `mounts()`.

    Args:
        extraOptions (dict[str, Any], optional): Additional options for listing mounts. Defaults to {}.

    Returns:
        list: The array of MountPointInfo.
    """
    return []


def refreshMounts():
    return False


def getMountPath(mountPoint, scope=""):
    return False


def fastcp(
    src: str, dest: str, recurse: bool = True, extraConfigs: dict[str, Any] = {}
) -> bool:
    """Copies a file or directory via azcopy, possibly across FileSystems.

    Examples::

        fastcp("file:/tmp/my-folder/a", "adls://xxx/tmp/b")
        fastcp("file:/tmp/my-folder/a", "adls://xxx/tmp/b", recurse=True, extraConfigs={"flags": "--disable-auto-decoding --follow-symlinks", "timeout": 3600})

    Args:
        src (str): FileSystem URI of the source file or directory.
        dest (str): FileSystem URI of the destination file or directory.
        recurse (bool, optional): If true, all files and directories will be recursively copied. Defaults to True.
        extraConfigs (dict[str, Any], optional): Extra configs for azcopy, includes flags, timeout, aadToken, sourceLinkedService, destinationLinkedService.
            - flags: All options supported by azcopy can be specified with flags.
            - timeout: The timeout in seconds for the azcopy command.
            - aadToken: The Azure Active Directory token to use for authentication.
            - sourceLinkedService: The name of the linked service for the source. Only support in Synapse.
            - destinationLinkedService: The name of the linked service for the destination. Only support in Synapse.
            Defaults to {}.

    Returns:
        bool: True if all files were successfully copied.
    """
    return False


def nbResPath():
    return ""
