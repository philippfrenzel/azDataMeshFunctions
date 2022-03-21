import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

class azKeyVault:
  def __init__(
        self,
        keyVaultName: str
    ) -> None:
        self.keyVaultName = keyVaultName

