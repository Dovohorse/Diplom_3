import allure
from pages.base_page import UiPage
from locators.login_page_locator import LoginPageLocators

class LoginPage(UiPage):

    @allure.step('Ждем открытия страницы авторизации пользвателя')
    def wait_open_login_page(self):
        self.wait_visible(LoginPageLocators.EMAIL_INPUT)  

    @allure.step('Вводим email в поле email')
    def fill_email(self, email):
        self.send_keys_to_input(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Вводим пароль в поле пароль')
    def fill_password(self, password):
        self.send_keys_to_input(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_sumbit_button(self):
        self.do_click(LoginPageLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step('Авториризация пользователя')
    def auth_user(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_sumbit_button()

    