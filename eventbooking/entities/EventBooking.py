import pyodbc
import os
import datetime
from azure.identity import DefaultAzureCredential
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.engine import URL
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

connection_string = os.environ['SQLAZURECONNSTR_WWIF']
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

engine = create_engine(connection_url)

Base = declarative_base()

class EventBooking(Base):
  __tablename__ = "eventbooking"
  
  id = Column(Integer(), primary_key=True)
  
  FKDataproductId = Column(String(40), primary_key=False)
  DataproductId   = Column(String(40), nullable=False)
  Relation        = Column(String, nullable=False)
  Status          = Column(String, nullable=False)
  created_at      = Column(DateTime(timezone=True), nullable=False, default=func.now())
  updated_at      = Column(DateTime, default=str("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  
  def __repr__(self):
        return f"Dataproduct(RootDataproduct={self.FKDataproductId!r}, relation={self.Relation!r}, ChildDataproduct={self.DataproductId!r})"

Base.metadata.create_all(engine)