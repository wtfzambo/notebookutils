def run(
    artifactId: str,
    functionName: str,
    parameters: {} = None,
    workspaceId: str = "",
    capacityId: str = "",
):
    """
    Run a User data functions (UDF).
    :param artifactId: The UDF artifact id.
    :param functionName: The UDF function name.
    :param parameters: The UDF parameters.
    :param workspaceId: The UDF workspace id, if not provided, it will be retrieved from the current workspace.
    :param capacityId: The UDF capacity id, if not provided, it will be retrieved from the current capacity.
    :return: The UDF execution result.
    """
    pass


def help(method=None):
    pass
