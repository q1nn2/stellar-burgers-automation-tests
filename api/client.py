import allure
import requests

from data.test_data import REQUEST_TIMEOUT
from data.urls import Urls


class StellarBurgersApi:
    @allure.step("Создать пользователя")
    def create_user(self, payload):
        return requests.post(
            Urls.REGISTER_USER,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step("Авторизовать пользователя")
    def login_user(self, payload):
        return requests.post(
            Urls.LOGIN_USER,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step("Удалить пользователя")
    def delete_user(self, access_token):
        return requests.delete(
            Urls.USER_DATA,
            headers={"Authorization": access_token},
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step("Получить ингредиенты")
    def get_ingredients(self):
        return requests.get(
            Urls.INGREDIENTS,
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step("Создать заказ")
    def create_order(self, payload, access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token

        return requests.post(
            Urls.ORDERS,
            json=payload,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
        )
