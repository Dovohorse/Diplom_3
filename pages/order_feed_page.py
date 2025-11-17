import allure
from pages.base_page import UiPage
from locators.order_feed_page_locators import FeedBoardLocators
from locators.order_feed_page_locators import FeedBoardLocators


class FeedBoard(UiPage):

    @allure.step('Количество заказов за всего')
    def total_orders_value(self):
        return self.get_text_element(FeedBoardLocators.TOTAL_ORDERS_COUNTER)

    @allure.step('Количество заказов за сегодня')
    def today_orders_value(self):
        return self.get_text_element(FeedBoardLocators.TODAY_ORDERS_COUNTER)
    
    @allure.step('Проверяем, что количество заказов увеличилось')
    def assert_orders_increased(self, count_after, count_before):
        return int(count_after) > int(count_before)

    @allure.step('Проверяем, что номер заказа появляется в разделе "В работе"')
    def is_order_in_progress(self, order_number):
        return self.scroll_to_element(FeedBoardLocators.order_number_in_order_history(order_number))
