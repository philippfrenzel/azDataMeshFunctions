import pyodbc
import os
import datetime
from azure.identity import DefaultAzureCredential
from jsonschema import validators, Draft4Validator, FormatChecker
from jsonschema.exceptions import ValidationError
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.engine import URL
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

connection_string = os.environ['SQLAZURECONNSTR_WWIF']
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

engine = create_engine(connection_url)

Base = declarative_base()

class EventBookingEntity(Base):
  __tablename__ = "eventbooking"
  
  id = Column(Integer(), primary_key=True)
  
  FKDataproductId = Column(String(40), primary_key=False)
  DataproductId   = Column(String(40), nullable=False)
  Relation        = Column(String, nullable=False)
  Status          = Column(String, nullable=False)
  created_at      = Column(DateTime(timezone=True), nullable=False, default=func.now())
  updated_at      = Column(DateTime, default=str("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

  def validate_json(self,json_body):
     schema = {
        'type': 'object',
        'properties': {
            'value': {
                'type': 'float',
                'format': 'even',
                'is_positive': True
            },
          }
        }
     
     # Define custom validators. Each must take exactly 4 arguments as below.
     def is_positive(validator, value, instance, schema):
        if not isinstance(instance, Number):
            yield ValidationError("%r is not a number" % instance)
        
        if value and instance <= 0:
            yield ValidationError("%r is not positive integer" % (instance,))
        elif not value and instance > 0:
            yield ValidationError("%r is not negative integer nor zero" % (instance,))
     
     # Add your custom validators among existing ones.
     all_validators = dict(Draft4Validator.VALIDATORS)
     all_validators['is_positive'] = is_positive

     # Create a new validator class. It will use your new validators and the schema
     # defined above.
     MyValidator = validators.create(
        meta_schema=Draft4Validator.META_SCHEMA,
        validators=all_validators
     )

     # Create a new format checker instance.
     format_checker = FormatChecker()
     # Register a new format checker method for format 'even'. It must take exactly one
     # argument - the value for checking.
     @format_checker.checks('even')
     def even_number(value):
        return value % 2 == 0
     # Create a new instance of your custom validator. Add a custom type.
     my_validator = MyValidator(
        schema, types={"float": float}, format_checker=format_checker
     )

     return my_validator.validate(json_body)

Base.metadata.create_all(engine)