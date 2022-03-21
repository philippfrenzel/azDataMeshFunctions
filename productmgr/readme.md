# Data Product Manager

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

