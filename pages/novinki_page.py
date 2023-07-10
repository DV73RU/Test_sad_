"""
Класс странице Новинки
"""
from base.base_class import BasePage


class NewsPage(BasePage):
    url = 'https://sad-i-ogorod.ru/catalog/novinki.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы элементов страницы.
    header_news = "//h1[@style='margin-bottom: 0px;']"
    info_wrapper = "//a[@class='prod-name js-prod-link-list']"  # Локатор карточки товара на старание продуктов.
    """
    Метод проверки заголовка странице
    """

    def check_news(self):
        self.check_page_header(self.header_news, "Новинки")  # Проверяем значение заголовка странице Новинки.
        self.parse_product(self.info_wrapper)  # Парсим товары на странице
        self.check_cart()  # Проверяем состояние иконнки корзины