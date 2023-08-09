# test_card.py
import pytest

from pages.card_pages import CardPage
from pages.main_page import MainPage
from pages.order_pages import OrderPage
from pages.order_pages_login import OrderPageLogin
from pages.seeds_page import SeedsPage

"""Параметр max_cart_total - сумма ограничения добавленных товаров"""


@pytest.mark.parametrize("max_cart_total", [800, 1500, 2500])
def test_add_to_card(driver, max_cart_total):
    print(f"Старт теста Добавление товаров в корзину с ограничением максимальной суммы: {max_cart_total}")

    main_page = MainPage(driver)
    main_page.check_main_page()  # Проверка URL главной станице
    main_page.go_seeds_pages()  # Переход на страницу "Семена" // TODO ДУБЛЬ ПРОВЕРОК URL

    seed_page = SeedsPage(driver)
    seed_page.check_page_seeds()  # Проверка странице "Семена"
    seed_page.parse_seeds()  # Парсинг товаров на странице "Семена"
    seed_page.add_to_card_in_seed(max_cart_total)  # Добавление товаров в корзину
    seed_page.go_card_pages()  # Переход на страницу Корзина

    card_page = CardPage(driver)
    card_page.check_card_page()  # Проверка заголовка старице корзина
    card_page.parse_card()  # Парсим товары в корзине
    card_page.check_logic_order(800, 2000)  # Проверяем логику ограничения суммы заказа
    if max_cart_total > 800:  # Кликаем на кнопку "Оформить заказ" только если сумма больше 800
        card_page.go_to_order()  # Переход на страницу оформления заказа
        order_page = OrderPage(driver)
        order_page.authorization()  # Авторизация
        order_page_login = OrderPageLogin(driver)
        order_page_login.check_pages()

