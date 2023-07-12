from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage

"""
Клас авторизованной странице.
"""


class MainPage(BasePage):
    url = 'https://sad-i-ogorod.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://sad-i-ogorod.ru/'
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # Локаторы.
    button_add_to_cart_locator = "//button[@class='to-cart-btn elem-to_cart']"
    product_price_locator = "//div[@class='prod-price ']"
    product_names = [...]  # Список названий продуктов
    button_card = "//span[@class = 'price']"  # Кнопка Корзина.
    # Количество товара в корзине.
    # Сумма заказа.
    button_novelties1 = "/html/body/div[1]/div[1]/div[4]/div/div/div[1]/a/span"  # Кнопка Новинки.
    button_novelties = "//a[@href='/catalog/novinki.html' and span[text()='Новинки']]"  # Кнопка Новинки.
    # // TODO button_add_card  перенести в base_class?
    button_add_card = "//button[@class ='to-cart-btn elem-to_cart']"  # Кнопка добавить в корзину, может пернести в base_class?
    agree_button = "//a[@class = 'cookie-msg__button']"  # Кнопка "Согласен" модального окна.

    # Меню Семена
    # Меню Плодовые
    # Меню Декоративные
    # Меню Луковичные
    # Кнопка Лук, чеснок
    # Кнопка Чай
    # Меню Сопутка

    def click_butt_novel(self):
        self.click_element(self.button_novelties1)  # Клик на кнопку Новинки в обход окна

    def click_butt_card(self):
        self.click_element(self.button_card)

    """
    Метод переход на станицу Новинки.
    Парсим товары на этой станице.
    Добавляем товары с этой странице.
    """



    def go_news_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_butt_novel()  # Кликаем на кнопку новинки.
        self.assert_url_2('https://sad-i-ogorod.ru/catalog/novinki.html')  # Проверка ожидаемой url



        # self.check_cart()  # Проверяем состояние иконнки корзины

    """
    Метод перехода в корзину
    """

    def go_to_card(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        self.click_butt_card()
        self.assert_url_2('https://sad-i-ogorod.ru/cart/')
