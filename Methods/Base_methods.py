import json
import requests
import allure
import random


class BaseMethods:

    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Получение гет запорса")
    def get_request(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        print(f"url = {url}")
        get_json = response.json()
        print(get_json)
        # response.raise_for_status()
        # return json.loads(response.content)

    @allure.step("Отправка пост запорса")
    def post_request(self, endpoint, data=None):
        url = self.base_url + endpoint
        json_data = {
                    "firstname" : "gasga",
                    "lastname" : "Brown",
                    "totalprice" : 111,
                    "depositpaid" : true,
                    "bookingdates" : {
                        "checkin" : "2018-01-01",
                        "checkout" : "2019-01-01"
                    },
                    "additionalneeds" : "Breakfast"
                }
        response = requests.post(url, json=json_data)
        response.raise_for_status()
        return json.loads(response.content)

    def put(self, endpoint, data=None):
        url = self.base_url + endpoint
        response = requests.put(url, json=data)
        response.raise_for_status()
        return json.loads(response.content)

    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url)
        response.raise_for_status()
        return json.loads(response.content)
