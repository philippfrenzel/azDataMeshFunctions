from services.keyvault_service import azKeyVault

def objKeyvault(keyVaultName):
    azkeyvault = azKeyVault(keyVaultName)
    pass

def test_objKeyvault():
    assert objKeyvault('MyKeyVault') == None

def getSecret(keyVaultName, secretName):
    azkeyvault = azKeyVault(keyVaultName)
    azkeyvault.getSecret(secretName)
    pass

def test_getSecret():
    assert eventBookingScan("MyKeyVault", "MyTestSecret") == None


