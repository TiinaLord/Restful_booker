from Methods.POST import PostRequest
import pytest


def test_post_booking(base_url):
    post_request_booking = PostRequest(base_url)
    post_request_booking.post_create_booking()


@pytest.mark.parametrize(("firstname", "lastname"),
                         [("Ssan", "Boown"), ("Erisa", "Willpower"), ("Martin", "Jacky"), ("Sandy", "Dick"),
                          ("Sam", "McCan"), ("Mark", "Nilson"), ("Terry", "Smith")])
def test_post_several_booking(base_url, firstname, lastname):
    post_request_booking = PostRequest(base_url)
    post_request_booking.post_create_several_booking(firstname, lastname)
