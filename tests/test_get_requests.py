from Restful_booker.Methods.GET import GetRequest
import pytest


def test_get_booking(base_url):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_endpoint()


def test_get_booking_with_params(base_url):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_endpoint()


@pytest.mark.parametrize("id_booking", ["1", "2", "3", "4", "5", "10", "101", "111", "222", "333"])
def test_get_booking_by_id(base_url, id_booking):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_by_id(id_booking)
