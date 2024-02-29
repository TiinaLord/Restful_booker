import random
import requests
from Base_methods import BaseMethods


class PostRequest(BaseMethods):
    def post_create_booking(self):
        self.post_request(endpoint="booking")

    @staticmethod
    def post_create_several_booking(firstname, lastname):
        url = "https://restful-booker.herokuapp.com/booking"
        json_data = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": random.randint(50, 800),
            "depositpaid": "true",
            "bookingdates": {
                "checkin": "2023-01-01",
                "checkout": "2024-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = requests.post(url, json=json_data)
        response.raise_for_status()
        get_json = response.json()
        print(get_json)
        assert response.status_code == 200
