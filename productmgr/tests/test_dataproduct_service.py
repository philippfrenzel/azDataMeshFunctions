from services.dataproduct_service import Dataproduct

def eventRegisterDataproduct(dataproductId,dataproductName):
    dataproduct = Dataproduct(dataproductId)
    dataproduct.register(dataproductId,dataproductName)
    pass

def test_eventRegisterDataproduct():
    assert eventRegisterDataproduct('DataProduct1', 'Unser erstes Datenprodukt') == None

def eventGetMetadata(dataproductId):
    dataproduct = Dataproduct(dataproductId)
    dataproduct.getMetadata()
    pass

def test_eventGetMetadata():
    assert eventGetMetadata('DataProduct1') == None
