import pyodbc
import os
import datetime
from azure.identity import DefaultAzureCredential
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.engine import URL
from sqlalchemy.sql import func

connection_string = os.environ['SQLAZURECONNSTR_WWIF']
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

engine = create_engine(connection_url)

m = MetaData()
dataproduct_dependencies = Table('dbo.dataproduct_dependencies', m, 
          Column('FKDataproductId', String(40), primary_key=True),
          Column('DataproductId', String(40), nullable=False),
          Column('Relation', String, nullable=False),
          Column('Status', String, nullable=False),
          Column('CreatedAt', DateTime(timezone=True), default=func.now())
    )
m.create_all(engine)    