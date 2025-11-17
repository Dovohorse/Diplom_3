import allure
from pages.base_page import UiPage
from locators.header_components_locators import TopbarLocators
from locators.order_feed_page_locators import FeedBoardLocators
from curl import Urls
from selenium.webdriver.common.by import By


class Topbar(UiPage):

    @allure.step('Клик на кнопку "Лента заказов"')
    def go_to_feed(self):
        # ждём, пока исчезнет оверлей модалки, который может перехватывать клик в Firefox
        try:
            self.wait_for_absence(By.CSS_SELECTOR, '.Modal_modal_overlay__x2ZCr', timeout=5)
        except Exception:
            pass
        self.do_click(TopbarLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверяем, что текущий URL - страница "Лента заказов"')
    def is_on_feed(self):
        return self.current_url() == Urls.ORDER_FEED_PAGE 

    @allure.step('Ждем открытия страницы с лентой заказов')
    def wait_feed_open(self):
        self.wait_visible(FeedBoardLocators.WORK_AREA)

    @allure.step('Клик на кнопку "Конструктор"')
    def go_to_constructor(self):
        self.do_click(TopbarLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверяем, что текущий URL - главная страницы')
    def is_on_main(self):
        return self.current_url() == Urls.MAIN_PAGE
    
    @allure.step('Клик на кнопку "Личный кабинет"')
    def open_account(self):
        self.do_click(TopbarLocators.ACCOUNT_BUTTON)
