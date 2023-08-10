"""
Класс странице Ордер
"""

import time
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage


class OrderPage(BasePage):
    url = 'https://sad-i-ogorod.ru/cart/order/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # +--------------------------------------------+
    # |     Локаторы странице 'Оформить заказ'     |
    # +--------------------------------------------+

    header_order = "//div[@class = 'h2 pt_5 mb_15']"  # Заголовок странице
    radio_new = "//input[@id = 'showTypeNew']"  # Радио баттон 'Я новый покупатель'
    label_radio_new = "//div[@class='user-type']//span[text()='Я новый покупатель']"    # Метка радиo кнопки 'Я новый покупатель'
    radio_reg = "//input[@id = 'showTypeReg']"  # Радио баттон "Я уже зарегистрирован"
    label_radio_reg = "//div[@class='user-type']//span[text()='Я уже зарегистрирован']"  # Метка радиo кнопки 'Я уже зарегистрирован'

    # +--------------------------------------------+
    # |         Локаторы 'Я новый покупатель'      |
    # +--------------------------------------------+
    button_next = "//div[@class = 'btn js-next']"  # Кнопка Далее
    input_surname = "//input[@name = 'surname']"  # Фамилия
    input_name = "//input[@name='name']"  # Имя
    input_father = "//input[@name = 'father']"  # Отчество
    input_phone = "//input[@name = 'phone']"  # Номер телефона
    input_email = "//input[@name = 'email']"  # email

    # +---------------------------------------------+
    # |      Локаторы 'Я уже зарегистрирован'       |
    # +---------------------------------------------+

    input_login = "//input[@name = 'USER_LOGIN']"  # Поле ввода "Логин"
    input_pass = "//input[@name = 'USER_PASSWORD']"  # Поле ввода "Пароль"
    label_login = "//div[@class = 'form-email form-group']//label[@class='form-label']"  # Название поля ввода login
    label_pass = "//div[@class = 'form-pass form-group']//label[@class='form-label']"  # Название поля ввода Pass
    button_submit = "//button[@class = 'btn btn-blue']"  # Кнопка "Войти"

    # +--------------------------------------+
    # |            Actions                   |
    # +--------------------------------------+

    def check_order_header(self, expected_header):
        self.check_page_header(self.header_order, expected_header)  # Проверяем значение заголовка странице Корзина.

    def click_radio_bt_reg(self):
        self.click_radio(self.radio_reg, self.label_radio_reg)    # Клик радиобутнон "Я зарегистрирован"

    def click_radio_bt_new(self):
        self.click_radio(self.radio_new, self.label_radio_new)  # Клик радиобутон "Я новый покупатель"

    def check_input_name(self):
        self.get_text(self.input_name)  # Что введено в поле имя

    def check_input_surname(self):
        self.get_text(self.input_surname)  # Что введено в поле Фамилия

    def check_input_father(self):
        self.get_text(self.input_father)  # Что введено в поле отчество

    def check_input_email(self):
        self.get_text(self.input_email)  # Что введено в поле email

    def check_input_phone(self):
        self.get_text(self.input_phone)  # Что введено в поле телефон

    def input_user_name(self, login):  # Ввод Логина
        self.input_in(self.input_login, self.label_login, login)  # Водим логин

    def input_password(self, password):  # Водим пароль
        self.input_in(self.input_pass, self.label_pass, password)

    def click_button_submit(self):
        self.click_element(self.button_submit)  # Кликаем на кнопку "Войти"

    def close_pop_up_cooke(self):
        self.close_cookie_banner()  # Закрытие pop-up окна "Работа с куками"

    # +-----------------------------------------+
    # |       Методы Оформления заказа          |
    # +-----------------------------------------+

    """
    Метод авторизации
    """
    def authorization(self):
        self.check_order_header('Оформление заказа')
        self.close_pop_up_cooke()
        time.sleep(2)
        self.click_radio_bt_reg()
        self.input_user_name('testlessdns@gmail.com')
        self.input_password('zaqwsx123')
        self.click_button_submit()
