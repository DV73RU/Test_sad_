# login_page.py
"""
Класс странице Авторизации
"""
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage


class LoginPage(BasePage):
    url = 'https://sad-i-ogorod.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://sad-i-ogorod.ru/'
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # +---------------------------------------------+
    # | Локаторы элементов страницы авторизации     |
    # +---------------------------------------------+
    label_user = "//label[@class = 'form-label']"
    username_input = "//input[@name='USER_LOGIN']"  # Локатор поля ввода логина.
    password_input = "//input[@type='password']"  # Локатор поля ввода пароля.
    submit_button = "//button[@class = 'btn btn-blue']"  # Локатор кнопки "Войти".
    login_title = "//*[@id='modal-login']/div/div/div/div/div[1]/div"  # Локатор заголовка окна регистрации.
    login_button_b = "//span[@class = 'name']"  # Локатор кнопки "Личный кабинет" после авторизации.
    login_button_a = "//span[@class = 'cabinet']"  # Локатор кнопки "Личный кабинет" до авторизации.
    label_login = "//div[@class='form-email form-group']//label[contains(@class, 'form-label')]"  # Локатор название поля логин.
    label_pass = "//div[@class='form-pass form-group mb_15']//label[contains(@class, 'form-label')]"  # Локатор название поля пароль.
    button_add_card = "//button[@class ='to-cart-btn elem-to_cart']"  # Кнопка добавить в корзину.
    agree_button = "//a[@class = 'cookie-msg__button']"  # Кнопка "Согласен" модального окна.

    # +--------------------------------------+
    # |            Actions                   |
    # +--------------------------------------+
    def click_login(self):  # Нажатие на кнопку "Личный кабинет"
        self.click_element(self.login_button_a)

    def input_user_name(self, user_name):  # Ввод в поле ввода Login
        self.input_in(self.username_input, self.label_login, user_name)

    def input_user_password(self, password):  # Ввод в поле ввода password
        self.input_in(self.password_input, self.label_pass, password)

    def click_submit_button(self):  # Нажатие на кнопку "Войти"
        self.click_element(self.submit_button)

    def check_button_text_before(self, value):  # Проверка название кнопки до авторизации
        self.get_button_text(self.login_button_a, value)

    def check_button_text_after(self, value):  # Проверка название кнопки после авторизации
        self.get_button_text(self.login_button_b, value, before_auth=False)

    # +-----------------------------------------+
    # |       Методы странице  Авторизация      |
    # +-----------------------------------------+

    def authorization(self):    # Авторизация
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.assert_url(self.url)  # Проверка ожидаемой url
        self.check_button_text_before("Личный кабинет")  # Проверка текста кнопки Личный кабинет до авторизации
        self.click_login()  # Кликаем на кнопку "Личный кабинет"
        self.check_page_header(self.login_title, "Вход")  # Проверяем значение заголовка странице авторизации.
        self.input_user_name('testlessdns@gmail.com')  # Ввод логина
        self.input_user_password('zaqwsx123')  # Ввод пароля
        self.click_submit_button()  # Клик на кнопку "Войти"
        self.assert_url('https://sad-i-ogorod.ru/?login=yes')  # Проверка ожидаемой URL
        self.check_button_text_after("Тестимя Тестфамилия")  # Проверка текста кнопки Личный кабинет после авторизации
