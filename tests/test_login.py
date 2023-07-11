import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.card_pages import CardPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.novinki_page import NewsPage
from pages.order_pages import OrderPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# options.add_argument('--headless')  # Безголовый режим(без запуска браузера)

# @pytest.fixture()
def test_login(set_group):
    service = Service('H:\\Python.Selenium_lesson-1\\Python_selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    print("Старт теста")
    # login_page = LoginPage(driver)
    # login_page.authorization()  # Авторизация на странице.

    main_page = MainPage(driver)
    main_page.go_news_page()  # Переход на страницу "Новинки"

    news_pages = NewsPage(driver)
    # news_pages.check_page_header()  # Проверяем заголовок странице Новинки
    news_pages.check_news()  # Чекаем товары на странице Новинки.
    # news_pages.go_

    # card_page = CardPage(driver)
    # card_page.check_card()  # Проверка странице "Корзина"
    # card_page.go_to_order()     # Переход на страницу Оформление заказа

    # order_page = OrderPage(driver)
    # order_page.check_order()    # Проверка станице Оформление заказа
