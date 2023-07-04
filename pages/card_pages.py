from base.base_class import BasePage


class CardPage(BasePage):
    url = 'https://sad-i-ogorod.ru/cart/?login=yes'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Локаторы элементов страницы.
    header_card = "//div[@class = 'elem-heading']/h1"  # Заголовок станице Корзина
    total_price_card = "//div[@class='bask-page__parcelTotal']/span[@class='bask-page__parcelTotal-price']"  # Итоговая сумма в корзине
    # // TODO Перенести все локаторы корзины.

    """
    Метод проверки корзины
    """

    def check_card(self):
        self.check_page_header(self.header_card, "Корзина")  # Проверяем значение заголовка странице Корзина.
        self.parse_products_card(compare_prices=True)
