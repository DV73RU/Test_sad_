import pytest
import os
from platform import system
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

from pages.card_pages import CardPage
from pages.main_page import MainPage
from pages.order_pages import OrderPage
from pages.order_pages_login import OrderPageLogin
from pages.seeds_page import SeedsPage


# def test_add_to_card(driver):
#     print("Старт теста Добавление товаров в корзину")
#
#     main_page = MainPage(driver)
#     main_page.go_seeds_pages()
#     seed_page = SeedsPage(driver)
#     seed_page.check_seeds()
#     seed_page.parse_seeds()
#     seed_page.add_to_cart2(max_cart_total=1500)

# @pytest.mark.parametrize("max_cart_total", [700, 1000, 2200])
def test_add_to_card(driver):
    print(f"Старт теста Добавление товаров в корзину")

    main_page = MainPage(driver)
    main_page.go_seeds_pages()
    seed_page = SeedsPage(driver)
    seed_page.check_seeds()
    seed_page.parse_seeds()
    seed_page.add_to_card2(max_cart_total=1000)
    seed_page.click_to_card()
    card_page = CardPage(driver)
    card_page.check_card("Корзина")
    card_page.check_ur()
    card_page.parse_card()
    card_page.close_banner()
    card_page.go_to_order()
    order_page = OrderPage(driver)
    order_page.authorization()
    order_page_login = OrderPageLogin(driver)
    order_page_login.check_pages()