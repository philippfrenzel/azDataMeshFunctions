# Service Classes

## Event Booking Manager

Specification Initial Draft (POC):

1) The service will expose a API-Endpoint, that accepts a GET-Request (scan) with the dataproductId as parameter -> this will scan the core folder of the dataproduct for the meta.json file.
2) The service will check the constraints for circular references and throw error if one is identified -> informed will be the newest dataproduct.
3) The service will expose a API-Endpoint, that accepts a GET-Request (trigger-upstream) with the dataproductId as parameter -> will check for dependent dataproducts and calls the executions API with notice.


## ...
