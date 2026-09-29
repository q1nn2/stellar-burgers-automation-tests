import allure
from selenium.common.exceptions import TimeoutException

from data.urls import Urls
from locators.constructor_locators import ConstructorLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    @allure.step("Открыть конструктор")
    def go_to_constructor(self):
        self.click_js(HeaderLocators.CONSTRUCTOR_LINK)
        self.wait_visible(ConstructorLocators.TITLE)

    @allure.step("Открыть ленту заказов")
    def go_to_order_feed(self):
        self.click_js(HeaderLocators.ORDER_FEED_LINK)
        self.wait_url(Urls.FEED_PAGE)

    @allure.step("Дождаться загрузки конструктора")
    def wait_loaded(self):
        self.wait_visible(ConstructorLocators.TITLE)

    @allure.step("Проверить, что конструктор открыт")
    def is_loaded(self):
        return self.is_visible(ConstructorLocators.TITLE)

    @allure.step("Открыть детали булки R2-D3")
    def open_bun_details(self):
        self.click_js(ConstructorLocators.BUN_R2_D3)
        self.wait_visible(ConstructorLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Проверить, что окно ингредиента открыто")
    def is_ingredient_modal_open(self):
        return self.is_visible(ConstructorLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_js(ConstructorLocators.MODAL_CLOSE_BUTTON)
        self.wait_invisible(ConstructorLocators.INGREDIENT_MODAL)

    @allure.step("Проверить, что окно ингредиента закрыто")
    def is_ingredient_modal_closed(self):
        try:
            return self.wait_invisible(ConstructorLocators.INGREDIENT_MODAL)
        except TimeoutException:
            return False

    @allure.step("Получить счётчик начинки Protostomia")
    def get_filling_counter(self):
        counters = self.find_child_elements(
            ConstructorLocators.FILLING_PROTOSTOMIA,
            ConstructorLocators.INGREDIENT_COUNTER,
        )
        return int(counters[0].text) if counters else 0

    @allure.step("Добавить начинку Protostomia в заказ")
    def add_filling_to_order(self):
        self.drag_and_drop(
            ConstructorLocators.FILLING_PROTOSTOMIA,
            ConstructorLocators.CONSTRUCTOR_DROP_AREA,
        )

    @allure.step("Добавить булку R2-D3 в заказ")
    def add_bun_to_order(self):
        self.drag_and_drop(
            ConstructorLocators.BUN_R2_D3,
            ConstructorLocators.CONSTRUCTOR_DROP_AREA,
        )

    @allure.step("Дождаться изменения счётчика начинки")
    def wait_for_filling_counter(self, expected_value):
        return self.wait_until(
            lambda _: self.get_filling_counter() == expected_value
        )

    @allure.step("Создать заказ через конструктор")
    def create_order(self):
        self.add_bun_to_order()
        self.add_filling_to_order()
        self.click_js(ConstructorLocators.ORDER_BUTTON)
        self.wait_visible(ConstructorLocators.ORDER_MODAL_TEXT)

        def order_number_is_ready(_):
            value = self.get_text(ConstructorLocators.ORDER_NUMBER).strip()
            return value if value.isdigit() and value != "9999" else False

        order_number = self.wait_until(order_number_is_ready, timeout=30)
        self.click_js(ConstructorLocators.MODAL_CLOSE_BUTTON)
        self.wait_invisible(ConstructorLocators.INGREDIENT_MODAL)

        return order_number
