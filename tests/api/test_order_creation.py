from http import HTTPStatus

import allure

from data.messages import INGREDIENTS_REQUIRED, INTERNAL_SERVER_ERROR
from data.test_data import INVALID_INGREDIENT_HASH


@allure.suite("API: создание заказа")
class TestOrderCreation:
    @allure.title("Авторизованный пользователь создаёт заказ с ингредиентами")
    def test_create_order_with_authorization_success(
        self,
        api_client,
        created_user,
        ingredient_ids,
    ):
        response = api_client.create_order(
            {"ingredients": ingredient_ids},
            created_user["access_token"],
        )
        body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert body["success"] is True
        assert body["order"]["number"]

    @allure.title("Заказ с ингредиентами создаётся без авторизации")
    def test_create_order_without_authorization_success(
        self,
        api_client,
        ingredient_ids,
    ):
        response = api_client.create_order({"ingredients": ingredient_ids})
        body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert body["success"] is True
        assert body["order"]["number"]

    @allure.title("Заказ без ингредиентов не создаётся")
    def test_create_order_without_ingredients_returns_error(
        self,
        api_client,
        created_user,
    ):
        response = api_client.create_order(
            {"ingredients": []},
            created_user["access_token"],
        )
        body = response.json()

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert body["success"] is False
        assert body["message"] == INGREDIENTS_REQUIRED

    @allure.title("Заказ с неверным хешем ингредиента возвращает ошибку сервера")
    def test_create_order_with_invalid_ingredient_hash_returns_server_error(
        self,
        api_client,
        created_user,
    ):
        response = api_client.create_order(
            {"ingredients": [INVALID_INGREDIENT_HASH]},
            created_user["access_token"],
        )

        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
        assert INTERNAL_SERVER_ERROR in response.text
