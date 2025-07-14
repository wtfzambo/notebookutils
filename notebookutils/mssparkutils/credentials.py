"""
getToken(audience, name): returns AAD token for a given audience, name (optional)
isValidToken(token): returns true if token hasn't expired
getConnectionStringOrCreds(linkedService): returns connection string or credentials for linked service
getFullConnectionString(linkedService): returns full connection string with credentials
getPropertiesAll(linkedService): returns all the properties of a linked servicegetSPTokenWithCert(resource, authority, clientId, akvNameOrUri, certificateName): returns an access token for a service principal using a certificate stored in a AKV as the credential
getSPTokenWithCertLS(resource, authority, clientId, akvLinkedService, certificateName): returns an access token for a service principal using a certificate stored in a AKV linked service as the credential
getSecret(akvName, secret, linkedService): returns AKV secret for a given AKV linked service, akvName, secret key
getSecret(akvName, secret): returns AKV secret for a given akvName, secret key
getSecretWithLS(linkedService, secret): returns AKV secret for a given linked service, secret key
putSecret(akvName, secretName, secretValue, linkedService): puts AKV secret for a given akvName, secretName
putSecret(akvName, secretName, secretValue): puts AKV secret for a given akvName, secretName
putSecretWithLS(linkedService, secretName, secretValue): puts AKV secret for a given linked service, secretName
"""


def getToken(audience, name=""):
    return ""


def getConnectionStringOrCreds(linkedService):
    return ""


def getFullConnectionString(linkedService):
    return ""


def getPropertiesAll(linkedService):
    return ""


def getSPTokenWithCert(resource, authority, clientId, akvNameOrUri, certificateName):
    return ""


def getSPTokenWithCertLS(
    resource, authority, clientId, akvLinkedService, certificateName
):
    return ""


def getSecret(akvName, secret, linkedService=""):
    return ""


def getSecretWithLS(linkedService, secret):
    return ""


def putSecret(akvName, secretName, secretValue, linkedService=""):
    return ""


def putSecretWithLS(linkedService, secretName, secretValue):
    return ""


def isValidToken(token):
    return False


def configureAzureBlobStorageSASBased(linkedService, container, sparkSession):
    pass


def configureADLS2TokenBased(linkedService, sparkSession):
    pass


def configureADLS2SASBased(linkedService, sparkSession):
    pass


def configureADLS2AzureKeyVaultBased(
    akvLinkedService, storageAccountName, secretName, sparkSession
):
    pass


def tridentHelp():
    pass


def synapseHelp():
    pass


def help():
    pass
