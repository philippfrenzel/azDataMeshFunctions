from services.keyvault_service import KeyVault

def objKeyvault(clientId, keyVaultName, keyVaultSecret, tenantId):
    keyVaultUri = f"https://{keyVaultName}.vault.azure.net"
    return KeyVault(
        clientId,
        keyVaultUri,
        keyVaultSecret,
        tenantId
    )

def test_getSecret():
    assert objKeyvault('MyKeyVault') == None



