from services.eventbooking_service import EventBooking

def eventBookingScan(dataproductId):
    eventbooking = EventBooking(dataproductId)
    eventbooking.setScan()

def test_eventBookingScan():
    print("Testing DPNYTaxi")
    assert eventBookingScan('DPNYTaxi') == None

def eventBookingBlobInContainer(dataproductId):
    eventbooking = EventBooking(dataproductId)
    eventbooking.getBlobsInContainer()

def test_eventBookingScan():
    print("Testing DPNYTaxi Blob Listing")
    assert eventBookingBlobInContainer('DPNYTaxi') == None
