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
        self.url = 'https://sad-i-ogorod.ru/cart/?login=yes'  # Авторизованный url Корзины
        self.url_2 = 'https://sad-i-ogorod.ru/cart/'  # Не авторизованный url корзины
        self.url_3 = 'https://sad-i-ogorod.ru/cart/order/'
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # max_total_price = 800    # Минимальная сумма для заказа.

    # +---------------------------------------------+
    # | Локаторы элементов страницы Корзина         |
    # +---------------------------------------------+

    header_card = "//div[@class = 'elem-heading']/h1"  # Заголовок станице Корзина
    total_price_card = "//div[@class='bask-page__parcelTotal']/span[@class='bask-page__parcelTotal-price']"  #
    # Итоговая сумма в корзине
    button_order = "//button[@class = 'bask-page__orderTotal-btn']"  # Кнопка "Оформить заказ - активна"
    button_order_not = "//button[@class = 'bask-page__orderTotal-btn  bask-page__orderTotal-btn--disable']"  #
    # Кнопка Оформить заказ - не активна
    value_min_price = "//span[@class = 'bask-page__parcelTotal-minPrice']"  # Локатор минимальной суммы для заказа.
    value_price = "//span[@class = 'bask-page__orderTotal-price']"  # Локатор суммы заказа Семена.
    value_total_price = "//span[@class = 'bask-page__orderTotal-price']"  # Локатор общей суммы заказа
    free_shipping = "//span[@class = 'bask-page__parcelTotal-freeship']"  # Локатор текста бесплатной доставки

    product_list = "//tr[contains(@class, 'bask-item')]"  # Локатор товаров козины

    # // TODO Перенести все локаторы корзины.
    # +--------------------------------------+
    # |            Actions                   |
    # +--------------------------------------+

    """
    +----------------------------------+
    |       Метод проверки корзины     |
    +----------------------------------+
    """

    def check_card(self, expected_header):
        self.check_page_header(self.header_card, expected_header)  # Проверяем значение заголовка странице Корзина.

    def check_ur(self):
        self.assert_url(self.url_2)  # Проверяем ulr корзины.
        # // TODO Как проверять url если для авторизованной один не для авторизованной другой? Через параметры в тестах?
        # //

    def check_url_order(self):
        self.assert_url(self.url_3)

    def parse_card(self):
        self.parse_products_card(self.product_list, print_products=True)  # Парсим товары на странице Корзины

    # def click_button_order2(self):  # Клик на кнопку Оформить ордер если мешает pop-ap
    #     self.click_element(self.button_order)

    def click_button_order3(self):  # Клик на кнопку Оформить ордер

        self.click_checkout(self.button_order, self.button_order_not, self.value_min_price)

    def check_order(self):  # Проверка логики заказа с минимальной суммой
        self.order_logic(800)

    def click_button_order(self):
        self.click_element(self.button_order)

    def close_banner(self):
        self.close_cookie_banner()

    """
    Метод переход на станицу Оформление заказа.
    """

    def go_to_order(self):
        # self.driver.get(self.url_3)
        # self.driver.maximize_window()
        # self.scroll_pages_to_element(self.button_order)
        self.click_button_order()  # Кликаем на кнопку Ордер если активна.
        self.check_url_order()  # Проверка ожидаемой url
