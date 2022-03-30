from entities.EventBookingEntity import EventBookingEntity

def refEventBooking():
    DPDModel = EventBookingEntity()
    pass

def test_refEventBooking():
    print(f"Testing DPDM ORM with SQL Alchemy")
    assert refEventBooking() == None