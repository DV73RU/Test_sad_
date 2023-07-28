"""
Класс странице Семена
"""
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage


class SeedsPage(BasePage):
    url = 'https://sad-i-ogorod.ru/catalog/semena.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://sad-i-ogorod.ru/catalog/semena.html'
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # Локаторы элементов страницы.
    header_seeds = "//h1[@style='margin-bottom: 0px;']"  # Заголовок странице
    info_wrapper = "//a[@class='prod-name js-prod-link-list']"  # Локатор карточки товара на старание продуктов.
    card_button = "//span[@class ='price']"

    # Actions

    def go_url_pages(self):
        self.go_to_pages(self.url)

    #
    def check_seeds(self):
        self.check_page_header(self.header_seeds,
                               "Семена почтой в интернет магазине Сады России")  # Проверяем значение заголовка странице Новинки.

    def parse_seeds(self):
        self.parse_product(self.info_wrapper)  # Парсим товары на странице

    def add_card(self):
        self.add_to_card2()  # Добавление товара в корзину со странице семена

    def click_to_card(self):
        self.click_element(self.card_button)    # Кликаем на кнопку корзины.
