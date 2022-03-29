from models.eventbooking_service import EventBooking

def eventBookingScan(dataproductId):
    eventbooking = EventBooking(dataproductId)
    return eventbooking.setScan()

def test_eventBookingScan():
    print("Testing DPNYTaxi")
    assert eventBookingScan('DPNYTaxi') == None
