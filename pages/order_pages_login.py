"""
Класс авторизованной странице Оформление заказа
'"""
import allure
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage


class OrderPageLogin(BasePage):
    url = 'https://sad-i-ogorod.ru/cart/order/?login=yes'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # +--------------------------------------------+
    # |     Локаторы странице 'Оформить заказ'     |
    # +--------------------------------------------+

    header_order = "//div[@class = 'h2 pt_5 mb_15']"  # Заголовок странице
    label_personal_data = "//a[@class = 'order__tab order__tab--active']"  # Личные данные
    button_next = "//div[@class = 'btn js-next']"  # Кнопка Далее
    input_surname = "//input[@name = 'surname']"  # Фамилия
    input_name = "//input[@name = 'name']"  # Имя
    input_father = "//input[@name = 'father']"  # Отчество
    input_phone = "//input[@name = 'phone']"  # Номер телефона
    input_email = "//input[@name = 'email']"  # email
    input_email_2 = "//div[@class='form-group form-group--tooltip row form-block']//input[@name = 'email']"
    label_surname = "//div[@class='form-group row form-block '][1]//label[@class='form-label required']"  # Метка поля ввода Фамилия
    label_name = "//div[@class='form-group row form-block '][3]//label[@class='form-label required']"  # Метка поля Имя
    label_father = "//div[@class='form-group row form-block '][4]//label[@class='form-label required']"  # Метка поля Отчество
    label_phone = "//div[@class='form-group row form-block '][2]//label[@class='form-label required']"  # Метка поля Номер телефона
    label_email = "//div[@class='form-group form-group--tooltip row form-block']//label[@class='form-label required']"  # Метка поля email

    # +--------------------------------------+
    # |            Actions                   |
    # +--------------------------------------+
    def check_order(self, expected_header):
        self.check_page_header(self.header_order, expected_header)  # Проверяем значение заголовка странице Корзина.

    def check_input_name(self, expected_value):
        self.check_input_value(self.input_name, self.label_name, expected_value)  # Что введено в поле имя

    def check_input_surname(self, expected_value):
        self.check_input_value(self.input_surname, self.label_surname, expected_value)  # Что введено в поле Фамилия

    def check_input_father(self, expected_value):
        self.check_input_value(self.input_father, self.label_father, expected_value)  # Что введено в поле отчество

    def check_input_email(self, expected_value):
        self.check_input_value(self.input_email_2, self.label_email, expected_value)  # Что введено в поле отчество

    def check_input_phone(self, expected_value):
        self.check_input_value(self.input_phone, self.label_phone, expected_value)  # Что введено в поле отчество

    # +-----------------------------------------+
    # |       Методы главной Оформления заказа  |
    # +-----------------------------------------+
    def check_pages(self):
        with allure.step("Проверка введенных данных в поля ввода"):
            self.check_order("Оформление заказа")
            self.check_input_father('Тестотчество')
            self.check_input_name('Тестимя')  # Проверяем что введено в поле ввода Имя
            self.check_input_surname('Тестфамилия')
            # self.check_input_email('testlessdns@gmail.com') #// TODO не наход локатор поля ввода :(
            self.check_input_phone('+7 (927) 816-47-86')
