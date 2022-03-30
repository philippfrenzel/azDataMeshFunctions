import os

class KeyVault:
    def __init__(self
              ,keyVaultName
        ):
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential
        keyVaultUri = f"https://{keyVaultName}.vault.azure.net"
        credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=keyVaultUri, credential=credential)

    def getSecret(self, secret_name, secret_version='') -> str:
        retrieved_secret = self.client.get_secret(secret_name, secret_version)
        return retrieved_secret.value