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
$Env:AZURE_CLIENT_ID="<azClientId>"
$Env:AZURE_TENANT_ID="<azTenantId>"
$Env:AZURE_STORAGE_CONNECTION_STRING="<azTenantId>"
```

# Event Booking Manager

## General

## Security

-> https://github.com/Azure-Samples/active-directory-python-external-identities-api-connector-azure-function-validate

Basic Authentification is set by default within the project.

## Methods

### eventbooking-scan

## Testing

Testing is implemented via pytest. -> https://docs.pytest.org/en/7.1.x/

After you have installed the package, you can just run pytest in the commandline and the tests from the test folder are beeing executed.

# Datastructure

## Table dataproduct_dependencies

| Attribute   | Description |
| ----------- | ----------- |
| FKDataproductId | The ID of the dataproduct - must be unique within the environment |
| Relation | Relation Type can be "UPSTREAM" or "DOWNSTREAM" |
| DataproductId | The ID of the related dataproduct |
| Status | Status of the relation can be "ACTIVE" or "INACTIVE" |
| CreatedAt | Creation Timestamp of the relation |