import pytest
from Restful_booker.Methods.Base_methods import BaseMethods


class PostRequest(BaseMethods):
    def post_create_booking(self):
        self.post_request(endpoint="booking")
