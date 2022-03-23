from azure.identity import DefaultAzureCredential
import json
import os

class EventBooking:
  def __init__(
        self,
        dataproductId: str
    ) -> None:
        self.dataproductId = dataproductId

  def getDataproduct(
        self
    ) -> None:
      # fetch the information from the dataproduct manager
      pass
  
  def getBlobsInContainer(self):
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
    # DefaultAzureCredential -> greift auf Managed Identity die im System hinterlegt ist zu
    # Maneged Identity (e.g. azure function app) (runtime)
    credential = DefaultAzureCredential()
    # init variables
    storageAccountName = "stdataproduct01"
    containername = "dpcore"
    account_uri = f"https://{storageAccountName}.blob.core.windows.net/"
    try:
        # will scan the storage account core folder for the meta.json file
        blob_service_client = BlobServiceClient(account_url=account_uri, credential=credential)
        # Instantiate a new ContainerClient
        container_client = blob_service_client.get_container_client(containername)
        # Instantiate a new BlobClient
        blob_list = container_client.list_blobs()
        for blob in blob_list:
          print("\t" + blob.name)
    except Exception as e:
      print(e)
  
  def setScan(self):
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
    # DefaultAzureCredential -> greift auf Managed Identity die im System hinterlegt ist zu
    # Maneged Identity (e.g. azure function app) (runtime)
    credential = DefaultAzureCredential()
    # init variables
    storageAccountName = "stdataproduct01"
    containername = "dpcore"
    filename = f"{self.dataproductId}/product-metadata.json"
    account_uri = f"https://{storageAccountName}.blob.core.windows.net/"
    try:
        # will scan the storage account core folder for the meta.json file
        blob_service_client = BlobServiceClient(account_url=account_uri, credential=credential)
        # Instantiate a new ContainerClient
        container_client = blob_service_client.get_container_client(containername)
        # Instantiate a new BlobClient
        blob_client = container_client.get_blob_client(filename)
        try:
            download_stream = blob_client.download_blob()
            product_metadata = json.loads(download_stream.readall().decode("utf-8"))
            print("\t" + product_metadata)
        except ResourceNotFoundError:
            print("No blob found.")
    except Exception as e:
      print(e)

  def setUpstreamTrigger(
    self,
  ) -> None:
    # will lookup all dataproducts dependend on this dataproduct and send a notification call to the execution api
    pass
