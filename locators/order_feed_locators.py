from selenium.webdriver.common.by import By


class OrderFeedLocators:
    TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']")

    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за все время:']"
        "/following-sibling::p",
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за сегодня:']"
        "/following-sibling::p",
    )
    IN_PROGRESS_ORDERS = (
        By.CSS_SELECTOR,
        "ul[class*='OrderFeed_orderListReady'] li",
    )
