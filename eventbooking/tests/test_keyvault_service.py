from models.keyvault_service import KeyVault

def objKeyvault(keyVaultName):
    KeyVault(keyVaultName)
    pass

def test_objKeyvault():
    assert objKeyvault('kv1234567pplay') == None


def getSecret(keyVaultName,secret):
    KVault = KeyVault(keyVaultName)
    return KVault.getSecret(secret)

def test_getSecret():
    assert getSecret('kv1234567pplay',"pytest") == "esklappt"



