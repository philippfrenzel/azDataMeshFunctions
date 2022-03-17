import pyodbc
import os
import logging

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
    dataproductId,
    dataproductName,
    dataproductSubscription = 'tbd',
    dataproductRessourcegroup = 'tbd',
    dataproductStorageAccount = 'tbd'
  ) -> None:
    self.dataproductName = dataproductName
    record = (self.dataproductId, self.dataproductName)
    logging.info(record)
    sql = """INSERT INTO dbo.dataproduct ([DataproductId], [Dataproduct Name]) VALUES (?, ?) """
    with pyodbc.connect(os.environ['SQLAZURECONNSTR_WWIF']) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,record)
    self.dataproductSubscription = dataproductSubscription
    self.dataproductRessourcegroup = dataproductRessourcegroup
    self.dataproductStorageAccount = dataproductStorageAccount
    
  def getMetadata(
      self
    ) -> None:
      pass