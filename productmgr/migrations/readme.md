# Config

## DB-Connection

Make sure you have Python 3.7 installed on your machine. Clone this repo in a directory on our computer and then create a virtual environment. For example:

```bash
virtualenv venv
```

then activate the created virtual environment. For example, on Windows:

```bash
.\venv\Scripts\activate
```

and then install all the required packages:

```bash
pip install -r requirements
```

Connection String should be added to the env on Windows: 

```bash
$Env:SQLAZURECONNSTR_WWIF="Driver={ODBC Driver 17 for SQL Server};Server=tcp:{server}.database.windows.net,1433;Database={database};UID={username};Authentication=ActiveDirectoryInteractive;"
```
