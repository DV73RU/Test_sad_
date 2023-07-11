"""
Класс странице Ордер
"""
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage


class OrderPage(BasePage):
    url = 'https://sad-i-ogorod.ru/cart/order/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://sad-i-ogorod.ru/'
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # Локаторы
    header_order = "//div[@class = 'h2 pt_5 mb_15']"    # Заголовок странице
    input_surname = "//input[@name = 'surname']"  # Фамилия
    input_name = "//input[@name='name']"  # Имя
    input_father = "//input[@name = 'father']"     # Отчество
    input_phone = "//input[@name = 'phone']"    # Номер телефона
    input_email = "//input[@name = 'email']"    # email
    button_next = "//div[@class = 'btn js-next']"   # Кнопка Далее
    # // TODO Проверка заполненности полей

    # Actions
    """
    Метод проверки заголовка странице Ордер
    """

    def check_order(self):
        self.check_page_header(self.header_order, "Оформление заказа")  # Проверяем значение заголовка странице Корзина.

    def check_input(self): # Возвращаем текст введённый в поля ввода.
        self.get_text(self.input_name)  # Что введено в поле имя
        self.get_text(self.input_surname)
        self.get_text(self.input_father)
        self.get_text(self.input_email)
        self.get_text(self.input_phone)
