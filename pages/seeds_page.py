# seeds_page.py
"""
Класс странице Семена
"""
import allure
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage
from pages.product_page import ProductPage
from utilities.logger import Logger


class SeedsPage(BasePage):
    url = 'https://sad-i-ogorod.ru/catalog/semena.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)
        self.max_card_total = 2000

    # +--------------------------------------------+
    # |     Локаторы странице 'Семена'             |
    # +--------------------------------------------+
    header_seeds = "//h1[@style='margin-bottom: 0px;']"  # Заголовок странице
    info_wrapper = "//a[@class='prod-name js-prod-link-list']"  # Локатор карточки товара на старание продуктов.
    card_button = "//span[@class ='price']"

    # +--------------------------------------+
    # |            Actions                   |
    # +--------------------------------------+

    #
    def check_seeds_header(self, expected_header):
        self.check_page_header(self.header_seeds, expected_header)  # Проверяем значение заголовка странице Семена.

    def parse_seeds(self):
        with allure.step("Парсим товары на странице Семена"):
            Logger.add_start_step(method="Парсим товары на странице Семена")
            self.parse_product(self.info_wrapper)  # Парсим товары на странице
            Logger.add_end_step(url=self.driver.current_url, method="Парсим товары на странице Семена")

    def click_to_card(self):
        self.click_element(self.card_button)  # Кликаем на кнопку корзины.

    def check_page_seeds(self):
        with allure.step("Проверка заголовка странице Семена"):
            Logger.add_start_step(method="Проверка заголовка странице Семена")
            self.check_seeds_header("Семена почтой в интернет магазине Сады России")
            Logger.add_end_step(url=self.driver.current_url, method="Проверка заголовка странице семена")
    # +----------------------------------+
    # |       Методы странице Семена     |
    # +----------------------------------+

    """
    Метод добавления товаров в корзину со странице Семена
    max_card_total - Ограничение заказа по сумме
    """
    def add_to_card_in_seed(self, max_card_total):
        with allure.step("Добавляем товар в корзину"):
            self.add_to_card(max_card_total, ProductPage.button_add_to_card, ProductPage.info_wrapper,
                             ProductPage.product_name, ProductPage.product_price)
    """
    Метод переход на старицу корзина
    """
    def go_card_pages(self):
        while allure.step("Переход в корзину"):
            self.click_to_card()  # Кликаем на кнопку корзины.
            self.assert_url('https://sad-i-ogorod.ru/cart/')  # Проверка ожидаемой url Корзины
