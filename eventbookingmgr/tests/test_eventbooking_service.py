from services.eventbooking_service import EventBooking

def eventBooking(dataproductId):
    eventbooking = EventBooking(dataproductId)

def test_eventBooking():
    assert eventBooking('DataProduct1') == None

def eventBookingScan(dataproductId):
    eventbooking = EventBooking(dataproductId)
    eventbooking.setScan()

def test_eventBookingScan():
    assert eventBookingScan('DataProduct1') == None

