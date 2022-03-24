import pyodbc
import os
from azure.identity import DefaultAzureCredential

with pyodbc.connect(os.environ['SQLAZURECONNSTR_WWIF']) as conn:
    with conn.cursor() as cursor:
        cursor.execute('''DROP TABLE IF EXISTS dbo.dataproduct_dependencies
CREATE TABLE dbo.dataproduct_dependencies(
	[FKDataproductId] nvarchar(40),
    [Relation] nvarchar(40),
    [DataproductId] nvarchar(40),
    [Status] nvarchar(40),
    [CreatedAt] datetime
)''')

    