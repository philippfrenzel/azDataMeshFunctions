import pyodbc
import os

with pyodbc.connect(os.environ['SQLAZURECONNSTR_WWIF']) as conn:
    with conn.cursor() as cursor:
        cursor.execute('''DROP TABLE IF EXISTS dbo.dataproduct
CREATE TABLE dbo.dataproduct(
	[DataproductId] nvarchar(40),
	[Dataproduct Name] nvarchar(60)
)''')
    with conn.cursor() as cursor:
        cursor.execute('''DROP TABLE IF EXISTS dbo.dataproduct_location
CREATE TABLE dbo.dataproduct_location(
	[FKDataproductId] nvarchar(40),
	[SubscriptionId] nvarchar(30),
    [RessourceGroupId] nvarchar(30),
    [StorageAccountId] nvarchar(30),
    [CreatedAt] datetime
)''')

    