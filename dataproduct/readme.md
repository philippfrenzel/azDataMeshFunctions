# Data Product Manager

# Storage Structure

To have a fixed starting and endpoint, each dataproduct has a representation within a storage account. The layers that are created by default within a azure data lake storage gen2:

container
/dpcore
/dpoutputport
/dpsource
/dpmeta

Here a quick draft on how the storage containers are used:

![data mesh storage concept](https://github.com/philippfrenzel/azDataMeshFunctions/blob/main/dataproduct/azDataMeshDPStorage.drawio.png)

## dpcore

Here we expect each dataproduct to exist as a parquet file(s).

## dpoutputport

All filebased outputports are placed within this folder.

## dpsource

Can be used for internal processing - not exposed outside of the dataproduct.

## dpmeta

Product Metadata as JSON-Format.

# Datastructure

## Table dataproduct

### Attributes

| Attribute   | Description |
| ----------- | ----------- |
| ID          | The ID of the dataproduct - must be unique within the environment |
| Name        | The human readable name of the dataproduct        |

## Table dataproduct_location

### Attributes

| Attribute   | Description |
| ----------- | ----------- |
| ID          | The ID of the dataproduct - must be unique within the environment |
| Subscription | The subscription in which the dataproduct is hosted |
| Ressourcegroup | The ressource group in which the dataproduct is hosted |
| Storage Account | The storage account in which the core of the dataproduct is hosted |

# Classes

## dataproduct_service.py

### Methods

#### Register Dataproduct

URI: /dataproduct/register?dpid=123456

