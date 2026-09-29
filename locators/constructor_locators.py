from selenium.webdriver.common.by import By

from data.ingredient_data import BUN_R2_D3_ID, FILLING_PROTOSTOMIA_ID


class ConstructorLocators:
    TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")

    BUN_R2_D3 = (
        By.CSS_SELECTOR,
        f"a[href='/ingredient/{BUN_R2_D3_ID}']",
    )
    FILLING_PROTOSTOMIA = (
        By.CSS_SELECTOR,
        f"a[href='/ingredient/{FILLING_PROTOSTOMIA_ID}']",
    )
    INGREDIENT_COUNTER = (
        By.CSS_SELECTOR,
        "p[class*='counter_counter__num']",
    )

    CONSTRUCTOR_DROP_AREA = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]",
    )
    ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Оформить заказ']",
    )

    INGREDIENT_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]",
    )
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//h2[normalize-space()='Детали ингредиента']",
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//button[contains(@class, 'Modal_modal__close')]",
    )

    ORDER_MODAL_TEXT = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//*[normalize-space()='Ваш заказ начали готовить']",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//h2[contains(@class, 'Modal_modal__title')]",
    )
