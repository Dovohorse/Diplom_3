import pytest
import allure
from pages.main_page import BurgerBuilder
from data import *


@allure.sub_suite('class TestConstructorFlow: Проверки работы Конструктора')
class TestConstructorFlow:

    @allure.title('Открывается модальное окно для одного выбранного ингредиента')
    def test_modal_shows_for_one_ingredient(self, browser):
        sample_id = INGREDIENTS[0]["id"]
        sample_name = INGREDIENTS[0]["name"]
        allure.dynamic.description(f"Кликаем по '{sample_name}' и ожидаем появление окна с деталями.")
        builder = BurgerBuilder(browser)
        builder.tap_ingredient_tile(sample_id)
        assert builder.is_ingredient_modal_visible(sample_id), f"Окно деталей для '{sample_name}' не появилось"

    @allure.title('Модальное окно закрывается по клику на крестик')
    def test_modal_closes_with_cross(self, browser):
        sample_id = INGREDIENTS[0]["id"]
        sample_name = INGREDIENTS[0]["name"]
        builder = BurgerBuilder(browser)
        builder.tap_ingredient_tile(sample_id)
        builder.close_modal_via_cross()
        assert builder.modal_is_closed(), f"Окно '{sample_name}' не закрылось по крестику"

    @allure.title('Счётчик увеличивается для одного выбранного ингредиента')
    @allure.description('Для булки счётчик должен увеличиться на 2.')
    def test_counter_updates_for_one_item(self, browser):
        builder = BurgerBuilder(browser)
        bun_id = BUNS[0]["id"]
        expected_total = 2
        builder.put_ingredient_into_cart(bun_id)
        assert builder.ingredient_counter_equals(bun_id, expected_total), f"Счётчик не равен {expected_total}"
