import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Дождаться загрузки ленты заказов")
    def wait_loaded(self):
        self.wait_visible(OrderFeedLocators.TITLE)

    @allure.step("Проверить, что лента заказов открыта")
    def is_loaded(self):
        return self.is_visible(OrderFeedLocators.TITLE)

    @allure.step("Получить значение счётчика заказов за всё время")
    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить значение счётчика заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Дождаться увеличения счётчика заказов за всё время")
    def wait_total_orders_increase(self, initial_value):
        return self.wait_until(
            lambda _: self.get_total_orders_count() > initial_value,
            timeout=30,
        )

    @allure.step("Дождаться увеличения счётчика заказов за сегодня")
    def wait_today_orders_increase(self, initial_value):
        return self.wait_until(
            lambda _: self.get_today_orders_count() > initial_value,
            timeout=30,
        )

    @staticmethod
    @allure.step("Нормализовать номер заказа")
    def _normalize_order_number(value):
        digits = "".join(character for character in value if character.isdigit())
        return str(int(digits)) if digits else ""

    @allure.step("Получить номера заказов в блоке 'В работе'")
    def get_in_progress_order_numbers(self):
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS)
        numbers = []

        for element in elements:
            number = self._normalize_order_number(element.text)
            if number:
                numbers.append(number)

        return numbers

    @allure.step("Проверить наличие заказа в блоке 'В работе'")
    def is_order_in_progress(self, order_number):
        expected = self._normalize_order_number(str(order_number))
        return expected in self.get_in_progress_order_numbers()

    @allure.step("Дождаться заказа в блоке 'В работе'")
    def wait_order_in_progress(self, order_number):
        return self.wait_until(
            lambda _: self.is_order_in_progress(order_number),
            timeout=30,
        )
