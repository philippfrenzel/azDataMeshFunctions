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