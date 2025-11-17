from selenium.webdriver.common.by import By

# Локаторы элементов из шапки страниц
class TopbarLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор"
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']") # Кнопка "Лента заказов"
