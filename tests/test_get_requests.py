from Restful_booker.Methods.GET import GetRequest


def test_get_booking(base_url):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_endpoint()


def test_get_booking_with_params(base_url):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_endpoint()


def test_get_booking_by_id(base_url):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_by_id()
