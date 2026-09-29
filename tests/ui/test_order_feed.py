import allure


@allure.suite("UI: лента заказов")
class TestOrderFeed:
    @allure.title("Новый заказ увеличивает счётчик 'Выполнено за все время'")
    def test_new_order_increases_total_counter(self, created_order_context):
        feed_page = created_order_context["feed_page"]
        initial_count = created_order_context["initial_total"]

        feed_page.wait_total_orders_increase(initial_count)

        assert feed_page.get_total_orders_count() > initial_count

    @allure.title("Новый заказ увеличивает счётчик 'Выполнено за сегодня'")
    def test_new_order_increases_today_counter(self, created_order_context):
        feed_page = created_order_context["feed_page"]
        initial_count = created_order_context["initial_today"]

        feed_page.wait_today_orders_increase(initial_count)

        assert feed_page.get_today_orders_count() > initial_count

    @allure.title("Номер нового заказа появляется в блоке 'В работе'")
    def test_new_order_appears_in_progress(self, created_order_context):
        feed_page = created_order_context["feed_page"]
        order_number = created_order_context["order_number"]

        feed_page.wait_order_in_progress(order_number)

        assert feed_page.is_order_in_progress(order_number)
