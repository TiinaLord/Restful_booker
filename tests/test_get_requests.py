from Methods.GET import GetRequest
import pytest


def test_get_booking(base_url):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_endpoint()


@pytest.mark.parametrize(("firstname", "lastname"),
                         [("Susan", "Brown"), ("Eric", "Wilson"), ("Mary", "Jackson"), ("Sally", "Jones"),
                          ("Sally", "Jones"), ("Mark", "Jones"), ("Mary", "Smith")])
def test_get_booking_with_params(base_url, firstname, lastname):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_endpoint_with_params(firstname, lastname)


@pytest.mark.parametrize("id_booking", ["1", "2", "3", "4", "5", "10"])
def test_get_booking_by_id(base_url, id_booking):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_booking_by_id(id_booking)

@pytest.mark.parametrize("id_booking", ["0", "-1", "9999", "test", ""])
def test_negative_get_booking_by_id(base_url, id_booking):
    get_request_booking = GetRequest(base_url)
    get_request_booking.get_negative_booking_by_id(id_booking)


def test_get_compare_json_by_booking_id(base_url):
    get_request_booking = GetRequest(base_url)
    get_request_booking.compare_json_with_file()

