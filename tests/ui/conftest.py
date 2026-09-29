from http import HTTPStatus

import pytest
from selenium import webdriver

from api.client import StellarBurgersApi
from data.browser_data import BROWSERS, WINDOW_HEIGHT, WINDOW_WIDTH
from data.urls import Urls
from pages.base_page import BasePage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from utils.generators import generate_user_data


@pytest.fixture(params=BROWSERS, ids=BROWSERS)
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
        browser = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)
        browser = webdriver.Firefox(options=options)
        browser.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {request.param}")

    BasePage(browser).go_to_url(Urls.HOME_PAGE)

    yield browser

    browser.quit()


@pytest.fixture
def constructor_page(driver):
    return ConstructorPage(driver)


@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def constructor_page_from_feed(constructor_page):
    constructor_page.go_to_order_feed()
    return constructor_page


@pytest.fixture
def opened_ingredient_modal(constructor_page):
    constructor_page.open_bun_details()
    return constructor_page


@pytest.fixture
def registered_ui_user():
    api_client = StellarBurgersApi()
    user_data = generate_user_data()
    response = api_client.create_user(user_data)

    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert body["success"] is True

    access_token = body["accessToken"]

    yield {
        "data": user_data,
        "access_token": access_token,
    }

    api_client.delete_user(access_token)


@pytest.fixture
def logged_in_driver(driver, registered_ui_user):
    login_page = LoginPage(driver)
    login_page.go_to_url(Urls.LOGIN_PAGE)
    login_page.login(
        registered_ui_user["data"]["email"],
        registered_ui_user["data"]["password"],
    )
    ConstructorPage(driver).wait_loaded()

    return driver


@pytest.fixture
def created_order_context(logged_in_driver):
    constructor_page = ConstructorPage(logged_in_driver)
    feed_page = OrderFeedPage(logged_in_driver)

    constructor_page.go_to_order_feed()
    feed_page.wait_loaded()

    initial_total = feed_page.get_total_orders_count()
    initial_today = feed_page.get_today_orders_count()

    constructor_page.go_to_constructor()
    order_number = constructor_page.create_order()

    constructor_page.go_to_order_feed()
    feed_page.wait_loaded()

    return {
        "feed_page": feed_page,
        "initial_total": initial_total,
        "initial_today": initial_today,
        "order_number": order_number,
    }
