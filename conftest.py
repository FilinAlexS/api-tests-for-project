import pytest
import requests
import allure
from jsonschema import validate


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get_api(self, url, params):
        res = f"{self.base_address}{url}"
        with allure.step(f"Отправили запрос к {res}"):
            return requests.get(res, params=params, headers=self.headers())

    @allure.epic('Filed tests')
    def get_api_fail(self, url, params):
        res = f'{self.base_address}{url}'
        with allure.step(f"Отправили запрос к {res}"):
            return requests.get(res, params=params)

    @staticmethod
    def validate_schema(response, schema):
        with allure.step("Проверка ответа на соответствие схеме"):
            validate(instance=response.json(), schema=schema)

    @staticmethod
    def check_status_code(response):
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code} код, " \
                                                f"подробнее: {response.text}"

    @staticmethod
    def headers():
        return {'x-access-token': '0bf89475db3bf28f09c630217e711ec2', }


@pytest.fixture
@allure.epic('Passed tests')
@allure.feature('API v1')
def travel_api_v1():
    return ApiClient(base_address="https://api.travelpayouts.com/v1/")


@pytest.fixture
@allure.epic('Passed tests')
@allure.feature('API v2')
def travel_api_v2():
    return ApiClient(base_address="https://api.travelpayouts.com/v2/prices/")
