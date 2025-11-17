import allure
from pages.header_components import Topbar


@allure.sub_suite ('class TestTopbarNavigation: Проверки навигации кнопок в шапке страницы')
class TestTopbarNavigation:

    @allure.title ('Переход по клику на кнопку "Конструктор" на главную страницу с разделом "Конструктор"')
    def test_goes_to_constructor_from_header(self, open_feed_first):
        navbar = Topbar(open_feed_first)
        navbar.go_to_constructor()
        assert navbar.is_on_main()

    @allure.title ('Переход по клику на кнопку "Лента заказов" в раздел "Лента заказов"')
    def test_opens_order_feed_from_header(self, browser):
        navbar = Topbar(browser)
        navbar.go_to_feed()
        assert navbar.is_on_feed()
