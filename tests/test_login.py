import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.card_pages import CardPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')  # Безголовый режим(без запуска браузера)

# @pytest.fixture()
def test_login(set_group):
    service = Service('H:\\Python.Selenium_lesson-1\\Python_selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    print("Старт теста")
    login_page = LoginPage(driver)
    login_page.authorization()  # Авторизация на странице.

    main_page = MainPage(driver)
    main_page.go_novinki()  # Переход на страницу "Новинки"
    main_page.go_to_card()  # Переход на станицу "Корзина"

    card_page = CardPage(driver)
    card_page.check_card()  # Проверка странице "Корзина"



