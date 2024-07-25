from Methods.POST import PostRequest
import pytest


def test_post_booking(base_url):
    post_request_booking = PostRequest(base_url)
    post_request_booking.post_create_booking()


@pytest.mark.parametrize(("firstname", "lastname"),
                         [("Ssan", "Boown"), ("Erisa", "Willpower"), ("Martin", "Jacky"), ("Sandy", "Dick"),
                          ("Sam", "McCan"), ("Mark", "Nilson"), ("Terry", "Smith")])
def test_post_booking_with_valid_names(base_url, firstname, lastname):
    post_request_booking = PostRequest(base_url)
    post_request_booking.post_create_several_booking(firstname, lastname)


@pytest.mark.parametrize(("firstname", "lastname"),
                         [("1", "2"), ("----", "____"), ("()", "1f13ugb138"), ("Русс", "Dick"),
                          ("/13jsf", "."), ("0", "&*(!*£$&)"), ('', '')])
def test_post_booking_with_symbols_numbers_as_string(base_url, firstname, lastname):
    post_request_booking = PostRequest(base_url)
    post_request_booking.post_create_several_booking(firstname, lastname)


@pytest.mark.parametrize(("firstname", "lastname"),
                         [("sfaaaaaaaaaaaaaaaaafasfsafasfsafasfafafsfafsafasfasfaf", "asfasfasfafafasfasfasfasfasfasfasfasfasfasfasfasfasf"), ("павшповшпррвпшпвшпрвшпшвпврпшвпршвпрвшпрвпвп", "ввыпрывгп0ывпиывгпрыгвпи0гывип0ыгвпиыщвопиышврпиывпиыовпищывопщывшптыьвп")])
def test_post_booking_with_long_names(base_url, firstname, lastname):
    post_request_booking = PostRequest(base_url)
    post_request_booking.post_create_several_booking(firstname, lastname)
