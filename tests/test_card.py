import pytest
import os
from platform import system
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

from pages.main_page import MainPage
from pages.seeds_page import SeedsPage


def test_add_to_card(driver):
    print("Старт теста Добавление товаров в корзину")

    main_page = MainPage(driver)
    main_page.go_seeds_pages()
    seed_page = SeedsPage(driver)
    seed_page.check_seeds()
    seed_page.parse_seeds()
    seed_page.add_to_cart2(max_cart_total=1500)
