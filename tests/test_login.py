# test_login.py
"""Тест авторизации"""
import pytest
from pages.card_pages import CardPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.seeds_page import SeedsPage


@pytest.mark.skip("Тест временно отключен")
def test_autorization(driver):
    print("Старт теста странице 'Семена'")
    main_page = MainPage(driver)
    main_page.go_seeds_pages()
    seed_page = SeedsPage(driver)
    seed_page.check_seeds()
    seed_page.parse_seeds()
    seed_page.add_to_cart(max_cart_total=1500)

    main_page = MainPage(driver)
    main_page.go_to_card()

    card_page = CardPage(driver)
    card_page.check_order()
    card_page.parse_card()
    card_page.go_to_order()
    card_page.check_card()


def test_authorization(set_group):
    print("Старт теста Авторизации")
    login_page = LoginPage(driver)
    login_page.authorization()

