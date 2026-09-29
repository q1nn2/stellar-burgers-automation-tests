from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//p[normalize-space()='Конструктор']/ancestor::a",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//p[normalize-space()='Лента Заказов']/ancestor::a",
    )
