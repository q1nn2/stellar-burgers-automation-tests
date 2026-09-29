import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Перейти на страницу")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться видимости элемента")
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться кликабельности элемента")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        self.wait_clickable(locator).click()

    @allure.step("Кликнуть по элементу через JavaScript")
    def click_js(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнить поле")
    def fill(self, locator, value):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(value)

    @allure.step("Дождаться перехода на URL")
    def wait_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    @allure.step("Дождаться исчезновения элемента")
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @allure.step("Проверить видимость элемента")
    def is_visible(self, locator):
        return self.wait_visible(locator).is_displayed()

    @allure.step("Найти элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Найти дочерние элементы")
    def find_child_elements(self, parent_locator, child_locator):
        parent = self.wait_visible(parent_locator)
        return parent.find_elements(*child_locator)

    @allure.step("Дождаться выполнения условия")
    def wait_until(self, condition, timeout=None):
        if timeout is None:
            return self.wait.until(condition)

        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_visible(source_locator)
        target = self.wait_visible(target_locator)

        self.driver.execute_script(
            """
            function createDragEvent(type) {
                const event = new CustomEvent(type, {
                    bubbles: true,
                    cancelable: true
                });
                event.dataTransfer = {
                    data: {},
                    setData: function(key, value) {
                        this.data[key] = value;
                    },
                    getData: function(key) {
                        return this.data[key];
                    }
                };
                return event;
            }

            const source = arguments[0];
            const target = arguments[1];

            const dragStart = createDragEvent('dragstart');
            source.dispatchEvent(dragStart);

            const drop = createDragEvent('drop');
            drop.dataTransfer = dragStart.dataTransfer;
            target.dispatchEvent(drop);

            const dragEnd = createDragEvent('dragend');
            dragEnd.dataTransfer = dragStart.dataTransfer;
            source.dispatchEvent(dragEnd);
            """,
            source,
            target,
        )
