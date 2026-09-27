from http import HTTPStatus

import allure
import pytest

from data.messages import REQUIRED_FIELDS, USER_ALREADY_EXISTS
from data.test_data import REQUIRED_USER_FIELDS


@allure.suite("API: создание пользователя")
class TestUserCreation:
    @allure.title("Уникальный пользователь успешно создаётся")
    def test_create_unique_user_success(self, created_user):
        response = created_user["response"]
        body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert body["success"] is True
        assert body["accessToken"]
        assert body["refreshToken"]

    @allure.title("Повторная регистрация существующего пользователя запрещена")
    def test_create_existing_user_returns_error(self, api_client, created_user):
        response = api_client.create_user(created_user["data"])
        body = response.json()

        assert response.status_code == HTTPStatus.FORBIDDEN
        assert body["success"] is False
        assert body["message"] == USER_ALREADY_EXISTS

    @pytest.mark.parametrize("missing_field", REQUIRED_USER_FIELDS)
    @allure.title("Регистрация без обязательного поля возвращает ошибку")
    def test_create_user_without_required_field_returns_error(
        self,
        api_client,
        user_data,
        missing_field,
    ):
        payload = user_data.copy()
        payload.pop(missing_field)

        response = api_client.create_user(payload)
        body = response.json()

        assert response.status_code == HTTPStatus.FORBIDDEN
        assert body["success"] is False
        assert body["message"] == REQUIRED_FIELDS
