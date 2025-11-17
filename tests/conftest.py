import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from pages.header_components import Topbar
from curl import *

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(Urls.MAIN_PAGE)
    elif request.param == "firefox":
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()

# Переход на страницу c разделом "Лента заказов"
@pytest.fixture
def open_feed_first(browser):
    topbar = Topbar(browser)
    topbar.go_to_feed()
    topbar.wait_feed_open()
    return browser
