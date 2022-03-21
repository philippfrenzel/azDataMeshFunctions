import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

class azKeyVault:
  def __init__(
        self,
        keyVaultName: str
    ) -> None:
        self.keyVaultName = keyVaultName
        keyVaultName = os.environ["KEY_VAULT_NAME"]
        KVUri = f"https://{keyVaultName}.vault.azure.net"

  def getSecret(
      self,
      secretName: str
    ) -> str:
      credential = DefaultAzureCredential()
      client = SecretClient(vault_url=self.KVUri, credential=credential)
      retrieved_secret = client.get_secret(secretName)
      return secretName