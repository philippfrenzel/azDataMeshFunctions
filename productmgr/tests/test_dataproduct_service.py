from services.dataproduct_service import Dataproduct

def eventRegisterDataproduct(dataproductId,dataproductName):
    dataproduct = Dataproduct(dataproductId)
    dataproduct.register(dataproductId,dataproductName)
    pass

def test_eventRegisterDataproduct():
    assert eventRegisterDataproduct('DataProduct1', 'Unser erstes Datenprodukt') == None
