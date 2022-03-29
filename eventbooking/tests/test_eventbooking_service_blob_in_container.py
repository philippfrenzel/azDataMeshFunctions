from models.eventbooking_service import EventBooking

def eventBookingBlobInContainer(dataproductId):
    eventbooking = EventBooking(dataproductId)
    eventbooking.getBlobsInContainer()

def test_eventBookingScan():
    print("Testing DPNYTaxi Blob Listing")
    assert eventBookingBlobInContainer('DPNYTaxi') == None
