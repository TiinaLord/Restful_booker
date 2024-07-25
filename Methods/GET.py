from Methods.Base_methods import BaseMethods
import allure
import json
from deepdiff import DeepDiff


class GetRequest(BaseMethods):

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

    def get_negative_booking_by_id(self, id_booking):
        self.get_invalid_request(endpoint=f"booking/{id_booking}")



    @allure.step("Сравнение JSON")
    def compare_json_with_file(self):
        data_from_url = self.get_request(endpoint=f"booking/{2}")
        with open('test_data/id2.json', "r") as file:
            data_from_file = json.load(file)
        diff = DeepDiff(data_from_file, data_from_url, ignore_order=True)
        if not diff:
            return "JSON идентичны"
        else:
            raise ValueError("JSON не идентичны")