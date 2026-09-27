from http import HTTPStatus

import pytest

from api.client import StellarBurgersApi
from utils.generators import generate_user_data


@pytest.fixture
def api_client():
    return StellarBurgersApi()


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def created_user(api_client):
    data = generate_user_data()
    response = api_client.create_user(data)

    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert body["success"] is True

    access_token = body["accessToken"]

    yield {
        "data": data,
        "response": response,
        "access_token": access_token,
    }

    api_client.delete_user(access_token)


@pytest.fixture
def ingredient_ids(api_client):
    response = api_client.get_ingredients()

    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert body["success"] is True
    assert body["data"]

    return [ingredient["_id"] for ingredient in body["data"][:2]]
