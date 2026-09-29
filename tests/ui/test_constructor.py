import allure

from data.urls import Urls


@allure.suite("UI: конструктор")
class TestConstructor:
    @allure.title("Клик по 'Конструктор' открывает конструктор")
    def test_click_constructor_opens_constructor(self, constructor_page_from_feed):
        constructor_page_from_feed.go_to_constructor()

        assert constructor_page_from_feed.is_loaded()

    @allure.title("Клик по 'Лента Заказов' открывает ленту заказов")
    def test_click_order_feed_opens_feed(self, constructor_page, order_feed_page):
        constructor_page.go_to_order_feed()
        order_feed_page.wait_loaded()

        assert order_feed_page.get_current_url() == Urls.FEED_PAGE

    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_click_ingredient_opens_details_modal(self, constructor_page):
        constructor_page.open_bun_details()

        assert constructor_page.is_ingredient_modal_open()

    @allure.title("Крестик закрывает окно с деталями ингредиента")
    def test_close_button_closes_ingredient_modal(self, opened_ingredient_modal):
        opened_ingredient_modal.close_ingredient_modal()

        assert opened_ingredient_modal.is_ingredient_modal_closed()

    @allure.title("Добавление ингредиента увеличивает его счётчик")
    def test_add_ingredient_increases_counter(self, constructor_page):
        initial_count = constructor_page.get_filling_counter()

        constructor_page.add_filling_to_order()
        constructor_page.wait_for_filling_counter(initial_count + 1)

        assert constructor_page.get_filling_counter() == initial_count + 1
