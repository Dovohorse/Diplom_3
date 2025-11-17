import pytest
import allure

from pages.order_feed_page import FeedBoard

from pages.header_components import Topbar
from pages.main_page import BurgerBuilder
from data import *
from selenium.webdriver.support.wait import WebDriverWait


@allure.sub_suite ('class TestFeedCounters: Проверки изменений в разделе "Лента заказов" после созданиия нового заказа')
class TestFeedCounters:


    @allure.title ('При создании нового заказа счётчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    @pytest.mark.parametrize("order_counter_method", [FeedBoard.total_orders_value, FeedBoard.today_orders_value])
    def test_counters_increase_after_order(self, open_feed_first, browser, order_counter_method):
        navbar = Topbar(open_feed_first)
        feed = FeedBoard(browser)

        # считаем до
        count_before = order_counter_method(feed)

        # создаём заказ через UI (1 булка)
        navbar.go_to_constructor()
        builder = BurgerBuilder(browser)
        ingredient_ids = [BUNS[0]["id"]]
        builder.place_order_via_ui(ingredient_ids, TEST_USER["email"], TEST_USER["password"])

        # возвращаемся в Ленту заказов
        navbar.go_to_feed()

        # ждём, пока счётчик увеличится
        WebDriverWait(browser, 20).until(lambda d: order_counter_method(feed) > count_before)
        count_after = order_counter_method(feed)
        assert feed.assert_orders_increased(count_after, count_before)

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_appears_in_progress(self, browser):
        builder = BurgerBuilder(browser)
        ingredient_ids = [BUNS[0]["id"]]
        order_number = builder.place_order_via_ui(ingredient_ids, TEST_USER["email"], TEST_USER["password"])
        topbar = Topbar(browser)
        topbar.go_to_feed()
        feed = FeedBoard(browser)        
        assert feed.is_order_in_progress(order_number)
