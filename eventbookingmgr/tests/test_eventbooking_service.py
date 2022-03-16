from services.eventbooking_service import EventBooking

def eventBooking(dataproductId):
    eventbooking = EventBooking(dataproductId)

def test_eventBooking():
    assert eventBooking('DataProduct1') == None
