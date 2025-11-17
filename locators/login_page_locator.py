from selenium.webdriver.common.by import By

# Локаторы страницы авторизации
class LoginPageLocators:

    EMAIL_INPUT = (By.NAME, "name") # Поле email
    PASSWORD_INPUT = (By.NAME, "Пароль") # Поле пароль
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти"

