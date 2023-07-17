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
    header_order = "//div[@class = 'h2 pt_5 mb_15']"  # Заголовок странице
    input_surname = "//input[@name = 'surname']"  # Фамилия
    input_name = "//input[@name='name']"  # Имя
    input_father = "//input[@name = 'father']"  # Отчество
    input_phone = "//input[@name = 'phone']"  # Номер телефона
    input_email = "//input[@name = 'email']"  # email
    button_next = "//div[@class = 'btn js-next']"  # Кнопка Далее
    button_submit = "//button[@class = 'btn btn-blue']"  # Кнопка "Войти"
    radio_new = "//input[@id = 'showTypeNew']"  # Радио баттон 'Я новый покупатель'
    radio_reg = "//input[@id = 'showTypeReg']"  # Радио баттон "Я уже зарегистрирован"
    # // TODO Проверка заполненности полей
    input_login = "//input[@name = 'USER_LOGIN']"  # Поле ввода "Логин"
    input_pass = "//input[@name = 'USER_PASSWORD']"  # Поле ввода "Пароль"

    # Actions
    """
    Метод проверки заголовка странице Ордер
    """

    def check_order(self):
        self.check_page_header(self.header_order, "Оформление заказа")  # Проверяем значение заголовка странице Корзина.

    def check_input_name(self):
        self.get_text(self.input_name)  # Что введено в поле имя

    def check_input_surname(self):
        self.get_text(self.input_surname)  # Что введено в поле Фамилия

    def check_input_father(self):
        self.get_text(self.input_father)  # Что введено в поле отчество

    def check_input_email(self):
        self.get_text(self.input_email)  # Что введено в поле отчество

    def check_input_phone(self):
        self.get_text(self.input_phone)  # Что введено в поле отчество

    def input_user_name(self, login):  # Ввод Логина
        self.input_in(self.input_login, login)  # Водим логин

    def input_password(self, password):  # Водим пароль
        self.input_in(self.input_password, password)

    def click_button_submit(self):
        self.click_element(self.button_submit)  # Кликаем на кнопку "Войти"

    def click_radio_new(self):  # Кликаем на "Я новый покупатель"
        self.click_element(self.radio_new)

    def click_radio_reg(self):  # Кликаем на "Я уже зарегистрирован"
        self.click_element(self.radio_reg)

    def authorization(self):
        self.click_radio_reg()
        self.input_user_name('testlessdns@gmail.com')
        self.input_password('zaqwsx123')
        self.click_button_submit()
