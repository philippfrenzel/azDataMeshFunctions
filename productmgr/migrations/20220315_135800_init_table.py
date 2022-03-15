import pyodbc
import os

with pyodbc.connect(os.environ['SQLAZURECONNSTR_WWIF']) as conn:
    with conn.cursor() as cursor:
        cursor.execute('''DROP TABLE IF EXISTS dbo.dataproduct
CREATE TABLE dbo.dataproduct(
	[Dataproduct ID] int,
	[Dataproduct Name] nvarchar(20)
)''')

    