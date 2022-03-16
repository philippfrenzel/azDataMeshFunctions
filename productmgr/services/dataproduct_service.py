import pyodbc

class Dataproduct:
  def __init__(
        self,
        dataproductId: str,
        dataproductName: str = "to be named"
    ) -> None:
        self.dataproductId = dataproductId
        self.dataproductName = dataproductName
      
  def register(
    self,
    dataproductName,
    dataproductSubscription,
    dataproductRessourcegroup,
    dataproductStorageAccount
  ) -> None:
    self.dataproductName = dataproductName
    self.dataproductSubscription = dataproductSubscription
    self.dataproductRessourcegroup = dataproductRessourcegroup
    self.dataproductStorageAccount = dataproductStorageAccount
    
  def getMetadata(
      self
    ) -> Other:
      pass