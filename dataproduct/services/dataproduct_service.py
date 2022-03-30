import pyodbc
import os
import logging
import json

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
    location_record = (self.dataproductId, self.dataproductSubscription, self.dataproductRessourcegroup, self.dataproductStorageAccount)
    location_sql = """INSERT INTO dbo.dataproduct_location ([FKDataproductId], [SubscriptionId], [RessourceGroupId], [StorageAccountId]) VALUES (?, ?, ?, ?) """
    with pyodbc.connect(os.environ['SQLAZURECONNSTR_WWIF']) as conn:
        with conn.cursor() as cursor:
            cursor.execute(location_sql,location_record)
    
  def getMetadata(
      self
    ):
      data = []
      location_sql = """SELECT [FKDataproductId], [SubscriptionId], [RessourceGroupId], [StorageAccountId] FROM dbo.dataproduct_location WHERE [FKDataproductId] = ? """
      with pyodbc.connect(os.environ['SQLAZURECONNSTR_WWIF']) as conn:
        with conn.cursor() as cursor:
            rows = cursor.execute(location_sql,self.dataproductId).fetchall()
            for row in rows:
                data.append([x for x in row])
      print(json.dumps(data))
      return json.dumps(data)
