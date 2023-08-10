"""
Класс странице Новинки
"""
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage


class NewsPage(BasePage):
    url = 'https://sad-i-ogorod.ru/catalog/novinki.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://sad-i-ogorod.ru/'
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # +---------------------------------------------+
    # | Локаторы элементов страницы Семена          |
    # +---------------------------------------------+
    header_news = "//h1[@style='margin-bottom: 0px;']"
    info_wrapper = "//a[@class='prod-name js-prod-link-list']"  # Локатор карточки товара на старание продуктов.

    # +--------------------------------------+
    # |            Actions                   |
    # +--------------------------------------+
    """
    Метод проверки заголовка странице
    """

    def check_news(self):
        self.check_page_header(self.header_news, "Новинки")  # Проверяем значение заголовка странице Новинки.

    def parse_news(self):
        self.parse_product(self.info_wrapper)  # Парсим товары на странице