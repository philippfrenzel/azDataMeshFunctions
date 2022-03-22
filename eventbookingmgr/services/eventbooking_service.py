import requests

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
      
  def setScan(
    self,
  ) -> None:
    # will scan the storage account core folder for the meta.json file
    response = requests.get("https://stdataproduct01.blob.core.windows.net/dpcore/DPNYTaxi/product-metadata.json?sp=r&st=2022-03-21T08:00:32Z&se=2022-03-21T16:00:32Z&spr=https&sv=2020-08-04&sr=b&sig=xyXmK5CBunnL5%2FcY7qa8SlpECuLhhGHEnU7IPvspFGY%3D")
    return response.json(), 201

  def setUpstreamTrigger(
    self,
  ) -> None:
    # will lookup all dataproducts dependend on this dataproduct and send a notification call to the execution api
    pass
