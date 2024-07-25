import json
import requests
import allure
import random
from faker import Faker
from datetime import timedelta


class BaseMethods:

    def __init__(self, base_url):
        self.base_url = base_url


    @allure.step("Отправка GET запорса")
    def get_request(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        print(f"url = {url}")
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Ошибка: {response.status_code}")

    @allure.step("Отправка невалидного GET запорса")
    def get_invalid_request(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        print(f"url = {url}")
        if response.status_code != 404:
            raise ValueError(f"Ошибка: {response.status_code}")
        else:
            return None

    @allure.step("Отправка POST запорса")
    def post_request(self, endpoint, data=None):
        url = self.base_url + endpoint

        fake = Faker()
        check_in_date = fake.date_between(start_date="-1y", end_date="today")
        stay_duration = fake.random_int(min=1, max=31)
        check_out_date = check_in_date + timedelta(days=stay_duration)

        json_data = {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "totalprice": random.randint(50, 800),
            "depositpaid": "true",
            "bookingdates": {
                "checkin": check_in_date.strftime("%Y-%m-%d"),
                "checkout": check_out_date.strftime("%Y-%m-%d")
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
