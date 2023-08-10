"""
Класс странице Корзина
"""

from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage


class CardPage(BasePage):
    url_reg = 'https://sad-i-ogorod.ru/cart/?login=yes'
    url = 'https://sad-i-ogorod.ru/cart/'
    url_order = 'https://sad-i-ogorod.ru/cart/order/'

    # min_cart_total = 800  # Минимальная сумма для оформления заказа
    # free_shipping_total = 2000  # Сумма заказа бесплатной доставки

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

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

    # +--------------------------------------+
    # |            Actions                   |
    # +--------------------------------------+

    def check_card_header(self, expected_header):
        self.check_page_header(self.header_card, expected_header)  # Проверяем значение заголовка странице Корзина.

    def check_url_order(self):
        self.assert_url(self.url_order)     # Проверка url "Оформление заказа"

    def parse_card(self):
        self.parse_products_card(self.product_list, print_products=True)  # Парсим товары на странице Корзины

    def click_button_order(self):
        self.click_element(self.button_order)   # Клик на кнопу "Оформить заказ"

    def go_to_order(self):  # Переход на страницу оформления заказа
        self.close_cookie_banner()  # Зарыть банер работы с куками
        self.click_button_order()  # Кликаем на кнопку Ордер если активна.
        self.check_url_order()  # Проверка ожидаемой url

    def check_card_page(self):
        self.check_card_header("Корзина")   # Проверка заголовка старице "Корзина"

    def check_text_shiing(self):
        self.check_text(self.free_shipping, "Бесплатная доставка")  # Проверка на кликабельность

    def check_text_shiing_min(self):
        self.check_text(self.free_shipping, "Бесплатная доставка от 2 000")  # Проверка наличие текста

    def check_text_min_order(self):
        self.check_text(self.min_price, "Минимальная стоимость посылки 800.0")  ## Проверка наличие текста

    def check_catalog_button_clickable(self):
        self.check_button_clickable(self.button_cat_seed, "Перейти в каталог семян")  # Проверка на кликабельность

    def check_order_button_not_clickable(self):
        self.close_cookie_banner()
        self.check_button_not_clickable(self.button_order_not, "Оформить заказ")  # Проверка Не кликабельность

    def check_order_button_clickable(self):
        self.check_button_clickable(self.button_order, "Оформить заказ")  # Проверка кликабельность

    # +----------------------------------+
    # |       Методы странице корзины    |
    # +----------------------------------+

    """
    Метод проверки бизнес логики "Ограничения в суммах заказа"`
    """

    def check_logic_order(self, min_cart_total, free_shipping_total):
        value_order_total = self.get_summ(self.total_price_card)  # Получаем сумму заказа
        if value_order_total <= min_cart_total:  # Если сумма заказа меньше
            print("Проверка бизнес логике: Заказ меньше 800\n==========================================")
            self.check_text_min_order()  # Проверяем наличия текста минимальной суммы
            self.check_catalog_button_clickable()  # Проверяем наличие и кликабельности кнопки "перейти в каталог"
            self.check_order_button_not_clickable()  # Проверяем не кликабельности кнопки "Оформить заказ"
            # pytest.skip()   # Пока пропустим
        elif min_cart_total < value_order_total < free_shipping_total:  # Если сумма заказа больше и меньше
            print("Проверка бизнес логике: Заказ больше 800 и меньше 2000\n==========================================")
            self.check_text_shiing_min()  # Проверка теста с предложением заказать на сумму бесплатной доставки
            self.check_order_button_clickable()  # Проверяем кликабельности кнопки "Оформить заказ"
        elif value_order_total >= free_shipping_total:
            print("Проверка бизнес логике: Заказ больше или равен 2000\n=========================================")
            self.check_text_shiing()  # Текст бесплатной доставки
            self.check_order_button_clickable()  # Проверяем не кликабельности кнопки "Оформит заказ"
