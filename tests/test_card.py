import pytest
import os
from platform import system
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

from pages.main_page import MainPage
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


def test_add_to_card(set_group):
    print("Старт теста Добавление товаров в корзину")

    main_page = MainPage(driver)
    main_page.go_seeds_pages()
    seed_page = SeedsPage(driver)
    seed_page.check_seeds()
    seed_page.parse_seeds()
    seed_page.add_to_cart2(max_cart_total=1500)

