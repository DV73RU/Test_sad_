"""
Класс странице Корзина
"""
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage


# // TODO написать описание

class CardPage(BasePage):
    url_reg = 'https://sad-i-ogorod.ru/cart/?login=yes'
    url = 'https://sad-i-ogorod.ru/cart/'
    url_order = 'https://sad-i-ogorod.ru/cart/order/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url_reg = 'https://sad-i-ogorod.ru/cart/?login=yes'  # Авторизованный url Корзины
        self.url = 'https://sad-i-ogorod.ru/cart/'  # Не авторизованный url корзины

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
    min_price = "//div[@class = 'bask-page__parcelTotal-minPriceError']//span"  # Локатор минимальной суммы для заказа.
    value_price = "//span[@class = 'bask-page__orderTotal-price']"  # Локатор суммы заказа Семена.
    value_total_price = "//span[@class = 'bask-page__orderTotal-price']"  # Локатор общей суммы заказа
    free_shipping = "//span[@class = 'bask-page__parcelTotal-freeship']"  # Локатор текста бесплатной доставки
    button_cat_seed = "//a[contains(text(), 'Перейти в каталог семян')]"  # Локатор Кнопки "Перейти в каталог семян"


    product_list = "//tr[contains(@class, 'bask-item')]"  # Локатор товаров козины

    # // TODO Перенести все локаторы корзины.
    # +--------------------------------------+
    # |            Actions                   |
    # +--------------------------------------+

    """
    +----------------------------------+
    |       Методы корзины             |
    +----------------------------------+
    """

    def check_card_header(self, expected_header):
        self.check_page_header(self.header_card, expected_header)  # Проверяем значение заголовка странице Корзина.

    def check_ur_card(self, url):
        self.assert_url(self.url)  # Проверяем ulr корзины.

    def check_url_order(self):
        self.assert_url(self.url_order)

    def parse_card(self):
        self.parse_products_card(self.product_list, print_products=True)  # Парсим товары на странице Корзины


    def click_button_order(self):
        self.click_element(self.button_order)

    def close_banner(self):
        self.close_cookie_banner()

    """
    Метод проверки заголовка странице Корзина 
    """
    def check_card_page(self):
        self.check_card_header("Корзина")

    """
    Метод переход на станицу Оформление заказа.
    """

    def go_to_order(self):
        self.click_button_order()  # Кликаем на кнопку Ордер если активна.
        self.check_url_order()  # Проверка ожидаемой url

    """
    Метод проверки бизнес логики "Ограничения в суммах заказа"
    """
    def check_order_total_2_2(self):  # TODO переименовать перед релизом
        total_element = self.get_element(self.total_price_card)     # Локатор суммы заказа
        total_element_text = total_element.text
        order_total = total_element_text.split(":")[1]
        value_order_total = int(order_total.replace('.00 i', '').replace(' ', ''))  # Удаляем лишние элементы из суммы.

        if value_order_total <= 800:    # Если сумма заказа меньше
            print("Проверка бизнес логике: Заказ меньше 800\n==========================================")
            self.check_min_order_text(self.min_price)  # Проверяем наличия текста минимальной суммы
            self.check_catalog_button(self.button_cat_seed)  # Проверяем наличие и кликабельности кнопки "перейти в каталог"
            self.check_order_button(self.button_order)   # Проверяем не кликабельности кнопки "Оформит заказ"
            pytest.skip()   # Пока пропустим
        elif 800 < value_order_total < 2000:  # Если сумма заказа больше и меньше
            print("Проверка бизнес логике: Заказ больше 800 и меньше 2000\n==========================================")
            self.check_order_button(self.button_order)   # Проверяем кликабельности кнопки "Оформить заказ"
        elif value_order_total >= 2000:
            print("Проверка бизнес логике: Заказ больше или равен 2000\n=========================================")
            ship_element = self.get_element(self.free_shipping)    # Текст бесплатной доставки
            assert "Бесплатная доставка" in ship_element.text
            print(f"На странице присутствует ожидаемый текст: {ship_element.text}")
            self.check_order_button(self.button_order)   # Проверяем не кликабельности кнопки "Оформит заказ"


