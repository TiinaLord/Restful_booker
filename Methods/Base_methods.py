import json
import requests
import allure
import random


class BaseMethods:

    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Получение GET запорса")
    def get_request(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        print(f"url = {url}")
        get_json = response.json()
        print(get_json)
        assert response.status_code == 200

    @allure.step("Отправка POST запорса")
    def post_request(self, endpoint, data=None):
        url = self.base_url + endpoint
        json_data = {
            "firstname": "Jes",
            "lastname": "Brown",
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

    @allure.step("Отправка PUT запорса")
    def put(self, endpoint, data=None):
        url = self.base_url + endpoint
        response = requests.put(url, json=data)
        response.raise_for_status()
        return json.loads(response.content)

    @allure.step("Отправка DELETE запорса")
    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url)
        response.raise_for_status()
        return json.loads(response.content)
