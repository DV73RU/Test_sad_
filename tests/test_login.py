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



# @pytest.fixture(driver)

# def test_seeds_pages2(driver):
#     print("Старт теста странице 'Семена'")
#     main_page = MainPage(driver)
#     main_page.go_seeds_pages()
#     seed_page = SeedsPage(driver)
#     seed_page.check_seeds()
#     seed_page.parse_seeds()
#     seed_page.add_to_cart(max_cart_total=1500)
#
#     main_page = MainPage(driver)
#     main_page.go_to_card()
#
#     card_page = CardPage(driver)
#     card_page.check_order()
#     card_page.parse_card()
#     card_page.go_to_order()
#     card_page.check_card()


# def test_authorization(set_group):
#     print("Старт теста Авторизации")
#     login_page = LoginPage(driver)
#     login_page.authorization()

