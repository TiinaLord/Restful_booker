from Restful_booker.Methods.POST import PostRequest


def test_get_booking(base_url):
    post_request_booking = PostRequest(base_url)
    post_request_booking.post_create_booking()
