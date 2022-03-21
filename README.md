# azDataMeshFunctions

(azure Data Mesh experience plane)

This repository will hold a sample implementation for the exprience planes of data mesh within azure using azure functions and python as scripting language.

# Getting Started

Move to the directory of the requirements.txt of the manager you wann work in / with.

Fetch required modules:

```bash
pip install -r requirements.txt
```

Start your own environment:

```bash
virtualenv env
```

Set your env variables:

```bash
$Env:SQLAZURECONNSTR_WWIF="Driver={ODBC Driver 17 for SQL Server};Server=tcp:{server}.database.windows.net,1433;Database={database};UID={username};Authentication=ActiveDirectoryInteractive;"
```


## Data Product Manager

The Data Product Manager is responsible for holding the current state and location of the data product.

## Event Booking Manager

# Security

## Basic Concept

-> https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python

