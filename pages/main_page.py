from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage

"""
Клас главной странице.
"""


class MainPage(BasePage):
    url = 'https://sad-i-ogorod.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # Локаторы.
    main_header = "//div[@class = 'main_hits_title']"
    button_add_to_cart_locator = "//button[@class='to-cart-btn elem-to_cart']"
    # product_price_locator = "//div[@class='prod-price ']"
    # product_names = [...]  # Список названий продуктов
    button_card = "//span[@class = 'price']"  # Кнопка Корзина если в ней есть товары
    button_card_f = "//span[@class='no-product']"  # Кнопка Корзины если в ней нет товаров
    # Количество товара в корзине.
    # Сумма заказа.
    button_novelties1 = "/html/body/div[1]/div[1]/div[4]/div/div/div[1]/a/span"  # Кнопка Новинки.
    button_novelties = "//a[@href='/catalog/novinki.html' and span[text()='Новинки']]"  # Кнопка Новинки.
    # // TODO button_add_card  перенести в base_class?
    button_add_card = "//button[@class ='to-cart-btn elem-to_cart']"  # Кнопка добавить в корзину, может пернести в base_class?
    agree_button = "//a[@class = 'cookie-msg__button']"  # Кнопка "Согласен" модального окна.
    button_seeds = "//a[@href='/catalog/semena.html' and span[text()='Семена']]"  # Кнопка Меню Семена

    # Локаторы карточки товара на странице
    add_to_cart_locator = "//button[@class='to-cart-btn elem-to_cart']"   # Локатор Кнопки добавить в корзину
    product_name_locator = ".//a[@class='prod-name js-prod-link-list']"   # Локатор название товара
    product_price_locator = ".//div[@class='prod-price ']"  # Локатор цены товара

    # Меню Плодовые
    # Меню Декоративные
    # Меню Луковичные
    # Кнопка Лук, чеснок
    # Кнопка Чай
    # Меню Сопутка

    def go_to_url_main_pages(self, url):
        self.go_to_url(self.url)

    def assert_url_main(self, expected_url):  # Проверка url главной с ожидаемым
        self.assert_url(self.url)

    def check_main_header(self, expected_header):
        self.check_page_header(self.main_header, expected_header)   # Проверка заголовка главной странице

    def click_butt_novel(self):
        self.click_element(self.button_novelties1)  # Клик на кнопку Новинки в обход окна

    def click_butt_seeds(self):
        self.click_element(self.button_seeds)  # Клик на кнопку Семена.

    def click_butt_card(self):
        self.click_element(self.button_card)  # Клик на кнопку Корзина.


    """
    Метод перехода на страницу Семена
    """

    def go_seeds_pages(self):
        self.click_butt_seeds()  # Кликаем на кнопку новинки.
        self.assert_url('https://sad-i-ogorod.ru/catalog/semena.html')  # Проверка ожидаемой url

    """
    Метод перехода в корзину
    """

    def go_to_card(self):
        self.click_butt_card() # Кликаем на кнопку Корзина.
        self.assert_url('https://sad-i-ogorod.ru/cart/')    # Проверка ожидаемой url

    def check_main_page(self):
        self.go_to_url_main_pages(self.url)
        self.assert_url_main("https://sad-i-ogorod.ru/")
        self.check_main_header('Хиты продаж')
