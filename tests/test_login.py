import pytest
import os
from platform import system
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

from pages.card_pages import CardPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.novinki_page import NewsPage
from pages.order_pages import OrderPage
from pages.seeds_page import SeedsPage

"""Методы обхода защиты от автоматизированного ПО в браузере Chrome под управлением Selenium в Python"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
exec_path = os.path.join(os.getcwd(), 'driver', 'chromedriver.exe') if system() == "Windows" else \
    os.path.join(os.getcwd(), 'driver', 'chromedriver')
driver = webdriver.Chrome(options=options, service=Service(log_path=os.devnull, executable_path=exec_path))

stealth(driver=driver,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/83.0.4103.53 Safari/537.36',
        languages=["ru-RU", "ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        run_on_insecure_origins=True,
        )


# options.add_argument('--headless')  # Безголовый режим(без запуска браузера)

# @pytest.fixture()
# def test_login(set_group):
#     service = Service('H:\\Python.Selenium_lesson-1\\Python_selenium\\chromedriver.exe')
#     # driver = webdriver.Chrome(options=options, service=Service(log_path=os.devnull, executable_path=exec_path))
#     # driver = webdriver.Chrome(service=service, options=options)
#     print("Старт теста")
#     # login_page = LoginPage(driver)
#     # login_page.authorization()  # Авторизация на странице.
#
#     main_page = MainPage(driver)
#     main_page.go_news_page()  # Переход на страницу "Новинки"
#
#     news_pages = NewsPage(driver)
#     # news_pages.check_page_header()  # Проверяем заголовок странице Новинки
#     news_pages.check_news()  # Чекаем товары на странице Новинки.
#     news_pages.parse_news()
#     news_pages.add_to_cart()
#     main_page.go_to_card()
#
#     card_page = CardPage(driver)
#     card_page.parse_card()
#
#     card_page.go_to_order()  # Переход на страницу Оформление заказа
#
#     order_page = OrderPage(driver)
#     order_page.check_order()  # Проверка станице Оформление заказа
#
#
# def test_seeds_pages(set_group):
#
#     print("Страт теста 'Семена'")
#     main_page = MainPage(driver)
#     main_page.go_seeds_pages()


def test_seeds_pages2(set_group):
    print("Старт теста странице 'Семена'")
    seed_page = SeedsPage(driver)
    seed_page.go_url_pages()
    seed_page.check_seeds()
    seed_page.parse_seeds()
    seed_page.add_to_cart(max_cart_total=1500)

    main_page = MainPage(driver)
    main_page.go_to_card()

    card_page = CardPage(driver)
    card_page.parse_card()
    card_page.go_to_order()
