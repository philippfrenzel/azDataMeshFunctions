# Service Classes

## Event Booking Manager

Specification Initial Draft (POC):

1) The service will expose a API-Endpoint, that accepts a GET-Request (scan) with the dataproductId as parameter -> this will scan the core folder of the dataproduct for the meta.json file.
2) The service will check the constraints for circular references and throw error if one is identified -> informed will be the newest dataproduct.
3) The service will expose a API-Endpoint, that accepts a GET-Request (trigger-upstream) with the dataproductId as parameter -> will check for dependent dataproducts and calls the executions API with notice.


## ...


# Helpers

## Azure Identity

https://azuresdkdocs.blob.core.windows.net/$web/python/azure-identity/1.8.0/index.html

## Azure Storage Blob

-> https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=environment-variable-windows
-> https://docs.microsoft.com/en-us/samples/azure/azure-sdk-for-python/storage-blob-samples/

