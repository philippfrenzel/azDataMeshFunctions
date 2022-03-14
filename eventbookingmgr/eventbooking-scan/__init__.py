import logging, json

import azure.functions as func
from services.eventbooking_service import EventBooking


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    eventBooking = EventBooking("DataProduct1")
    return func.HttpResponse(json.dumps(eventBooking), headers={"content-type": "application/json"})
