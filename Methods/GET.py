import pytest
import requests
from Restful_booker.Methods.Base_methods import BaseMethods


class GetRequest(BaseMethods):

    # def setup(self):
    #     self.base_url = BaseMethods(self.base_url)

    def get_booking_endpoint(self):
        self.get_request(endpoint="booking", params=None)

    def get_booking_endpoint_with_params(self, firstname, lastname):
        params = {
            "firstname": firstname,
            "lastname": lastname
        }
        self.get_request(endpoint="booking", params=params)

    def get_booking_by_id(self, id_booking):
        self.get_request(endpoint=f"booking/{id_booking}")
