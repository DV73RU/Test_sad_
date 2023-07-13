"""
Класс странице Корзина
"""
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage


# // TODO написать описание

class CardPage(BasePage):
    url = 'https://sad-i-ogorod.ru/cart/?login=yes'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://sad-i-ogorod.ru/'
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # max_total_price = 800    # Минимальная сумма для заказа.
    # Локаторы элементов страницы.
    header_card = "//div[@class = 'elem-heading']/h1"  # Заголовок станице Корзина
    total_price_card = "//div[@class='bask-page__parcelTotal']/span[@class='bask-page__parcelTotal-price']"  # Итоговая сумма в корзине
    button_order = "//button[@class = 'bask-page__orderTotal-btn']"  # Кнопка "Оформить заказ"
    product_list = "//tr[contains(@class, 'bask-item')]" # Локатор товаров козины
    # // TODO Перенести все локаторы корзины.

    # Actions
    """
    Метод проверки корзины
    """

    def check_card(self):
        self.check_page_header(self.header_card, "Корзина")  # Проверяем значение заголовка странице Корзина.

    def parse_card(self):
        self.parse_products_card(self.product_list, print_products= True)  # Парсим товары на странице Корзины

    def click_button_order2(self):  # Клик на кнопку Оформить ордер если мешает pop-ap
        self.click_element(self.button_order)

    """
    Метод переход на станицу Оформление заказа.
    """

    def go_to_order(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()
        self.click_button_order2()  # Кликаем на кнопку Ордер.
        self.assert_url_2('https://sad-i-ogorod.ru/cart/order/')  # Проверка ожидаемой url
