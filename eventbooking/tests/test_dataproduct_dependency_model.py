from models import DataproductDependencyModel

def refDataproductDependencyModel():
    DPDModel = DataproductDependencyModel()

def test_refDataproductDependencyModel():
    print("Testing DPDM ORM with SQL Alchemy")
    assert refDataproductDependencyModel() == None