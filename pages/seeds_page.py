# seeds_page.py
"""
Класс странице Семена
"""
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage
from pages.product_page import ProductPage


class SeedsPage(BasePage):
    url = 'https://sad-i-ogorod.ru/catalog/semena.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)
        self.max_card_total = 2000

    # Локаторы элементов страницы.
    header_seeds = "//h1[@style='margin-bottom: 0px;']"  # Заголовок странице
    info_wrapper = "//a[@class='prod-name js-prod-link-list']"  # Локатор карточки товара на старание продуктов.
    card_button = "//span[@class ='price']"

    # Actions

    #
    def check_seeds_header(self, expected_header):
        self.check_page_header(self.header_seeds, expected_header)  # Проверяем значение заголовка странице Семена.

    def parse_seeds(self):
        self.parse_product(self.info_wrapper)  # Парсим товары на странице

    def click_to_card(self):
        self.click_element(self.card_button)  # Кликаем на кнопку корзины.

    def check_page_seeds(self):
        self.check_seeds_header("Семена почтой в интернет магазине Сады России")

    def add_to_card_in_seed(self, max_card_total):
        self.add_to_card3(max_card_total, ProductPage.button_add_to_card, ProductPage.info_wrapper,
                          ProductPage.product_name, ProductPage.product_price)

    def go_card_pages(self):
        self.click_to_card()  # Кликаем на кнопку корзины.
        self.assert_url('https://sad-i-ogorod.ru/cart/')  # Проверка ожидаемой url Корзины
