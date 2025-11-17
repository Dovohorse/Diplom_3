import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.webdriver.common.by import By


class UiPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Ожидаем видимость элемента')
    def wait_visible(self, locator, timeout = 10):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ждём, пока элемент станет кликабельным")
    def wait_for_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
    
    @allure.step('Клик на элемент')
    def do_click(self, locator, timeout = 10):
        element = self.wait_for_clickable_element(locator,timeout)
        element.click()

    @allure.step('Получаем URL текущей страницы')
    def current_url(self):
        return self.browser.current_url

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_visible(locator, timeout)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    @allure.step("Ожидаем, что элемент исчезнет")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетаскиваем элемент на другой элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.scroll_to_element(source_locator)
        target = self.wait_visible(target_locator)
        drag_and_drop(self.browser, source, target)
        
    @allure.step('Вводим текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout = 10):
        element = self.wait_visible(locator,timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получаем текст элемента')
    def get_text_element(self, locator, timeout = 10):
        element = self.wait_visible(locator,timeout)
        return element.text
    
    @allure.step('Ждём появления элемента в DOM')
    def wait_for_element_present(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Клик через JS, если обычный click() не срабатывает')
    def click_js(self, locator):
        close_button = self.wait_for_element_present(locator)
        self.browser.execute_script("arguments[0].click();", close_button)


@allure.step('Ожидаем, что элемент исчезнет/станет невидимым')
def wait_for_absence(self, by, value, timeout=10):
    WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located((by, value)))
