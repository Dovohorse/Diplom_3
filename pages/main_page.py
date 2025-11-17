import allure
from pages.base_page import UiPage
from locators.main_page_locators import BuilderLocators
from pages.login_page import LoginPage


class BurgerBuilder(UiPage):

    @allure.step('Клик на карточку ингредиента: {ingredient_id}')
    def tap_ingredient_tile(self, ingredient_id):
        locator = BuilderLocators.locator_ingredient_card_by_id(ingredient_id)
        self.scroll_to_element(locator)
        self.do_click(locator)

    @allure.step('Проверяем, что появилось всплываюющее окно с деталями ингрединта')
    def is_ingredient_modal_visible(self, ingredient_id):
        locator = BuilderLocators.locator_ingredient_popup_by_id(ingredient_id)
        return self.wait_visible(locator)
    
    @allure.step("Кликаем на крестик в всплывающем окне с деталями ингредиента")
    def close_modal_via_cross(self):
        self.do_click(BuilderLocators.POPUP_CLOSE_BUTTON)

    @allure.step("Проверяем, что попап закрылся")
    def modal_is_closed(self):
        return self.wait_for_element_to_disappear(BuilderLocators.POPUP)
     
    @allure.step("Добавляем ингредиент '{ingredient_id}' в корзину")
    def put_ingredient_into_cart(self, ingredient_id):
        source = BuilderLocators.locator_ingredient_card_by_id(ingredient_id)
        target = BuilderLocators.CONSTRUCTOR_BASKET
        self.drag_and_drop(source, target)
    
    @allure.step("Получаем значение счётчика ингредиента '{ingredient_id}'")
    def get_ingredient_counter(self, ingredient_id, timeout=10):
        locator = BuilderLocators.locator_ingredient_counter(ingredient_id)
        counter_element = self.wait_visible(locator, timeout)
        return int(counter_element.text)

    @allure.step("Проверяем, что счётчик ингредиента '{ingredient_id}' равен {expected_count}")
    def ingredient_counter_equals(self, ingredient_id, expected_count, timeout=10):
        actual_count = self.get_ingredient_counter(ingredient_id, timeout)
        return actual_count == expected_count
    
    @allure.step('Клик на кнопку "Войти в аккаунт"')
    def click_login_button(self):
        self.do_click(BuilderLocators.LOGIN_BUTTON)

    @allure.step('Ждем открытия главной страницы с Конструктором')
    def wait_open_main_page(self):
        self.wait_visible(BuilderLocators.WORK_AREA)  

    @allure.step('Клик на кнопку "Оформить заказа"')
    def click_create_order_button(self):
        self.do_click(BuilderLocators.CREATE_ORDER_BUTTON)

    @allure.step('Ждем открытия окна с номером заказа')
    def wait_open_window_with_number(self):
        self.wait_visible(BuilderLocators.ORDER_NUMBER_IN_MODAL)

    @allure.step('Получаем номер заказа')
    def get_order_number(self, retries=10):
        locator = BuilderLocators.ORDER_NUMBER_IN_MODAL
        while True:
            order_number = self.get_text_element(locator)
            if order_number != "9999":
                break
        return order_number
    
    @allure.step('Клик на крестик(закрыть) в окне с номером заказа"')
    def click_close_order_button(self):
        self.wait_for_element_present(BuilderLocators. CLOSE_ORDER_MODAL_BUTTON)
        self.click_js(BuilderLocators. CLOSE_ORDER_MODAL_BUTTON)
        self.wait_for_element_to_disappear(BuilderLocators.MODAL_ORDER_WINDOW)

    @allure.step('Создание заказа c авторизацией пользователя')
    def place_order_via_ui(self, ingredient_ids, email, password):
        for ingredient_id in ingredient_ids:
            self.put_ingredient_into_cart(ingredient_id)
        self.click_login_button()
        login_page = LoginPage(self.browser)
        login_page.auth_user(email, password)
        self.click_create_order_button()
        order_number = self.get_order_number()
        self.click_close_order_button()
        return order_number
