import pytest
import requests
from Restful_booker.Methods.Base_methods import BaseMethods

class GetRequest(BaseMethods):

    # def setup(self):
    #     self.base_url = BaseMethods(self.base_url)

    def get_booking_endpoint(self):
        self.get_request(endpoint="booking", params=None)

    @pytest.mark.parametrize()
    def get_booking_endpoint_with_params(self):
        self.get_request(endpoint="booking")

    # @pytest.mark.parametrize("id_booking", [1, 2, 3, 4, 5, 10, 100, 111, 222, 333])
    # def get_booking_by_id(self, id_booking):
    #     self.get_request(endpoint="booking", params={"id_booking": id_booking})