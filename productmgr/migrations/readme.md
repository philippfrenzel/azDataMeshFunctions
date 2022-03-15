# Config

## DB-Connection

Connection String should be added to the env

Windows: 

$Env:SQLAZURECONNSTR_WWIF="Driver={ODBC Driver 17 for SQL Server};Server=tcp:{server}.database.windows.net,1433;Database={database};UID={username};Authentication=ActiveDirectoryInteractive;"