from http import HTTPStatus

import allure
import pytest

from data.messages import INVALID_CREDENTIALS
from data.test_data import INVALID_LOGIN_CASE_IDS, INVALID_LOGIN_CASES


@allure.suite("API: авторизация пользователя")
class TestUserLogin:
    @allure.title("Зарегистрированный пользователь успешно авторизуется")
    def test_login_existing_user_success(self, api_client, created_user):
        response = api_client.login_user(created_user["data"])
        body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert body["success"] is True
        assert body["accessToken"]
        assert body["refreshToken"]

    @pytest.mark.parametrize(
        "field, invalid_value",
        INVALID_LOGIN_CASES,
        ids=INVALID_LOGIN_CASE_IDS,
    )
    @allure.title("Авторизация с неверными учётными данными возвращает ошибку")
    def test_login_with_invalid_credentials_returns_error(
        self,
        api_client,
        created_user,
        field,
        invalid_value,
    ):
        payload = created_user["data"].copy()
        payload[field] = invalid_value

        response = api_client.login_user(payload)
        body = response.json()

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert body["success"] is False
        assert body["message"] == INVALID_CREDENTIALS
