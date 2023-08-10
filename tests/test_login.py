# test_login.py
"""Тест авторизации"""
import pytest
from pages.card_pages import CardPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.seeds_page import SeedsPage


# @pytest.mark.skip("Тест пропущен")
def test_authorization(driver):
    print("Старт теста Авторизации")
    login_page = LoginPage(driver)
    login_page.authorization()
