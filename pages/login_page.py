from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage


# // TODO написать описание
class LoginPage(BasePage):
    url = 'https://sad-i-ogorod.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://sad-i-ogorod.ru/'
        wait_timeout = 10  # Увеличьте время ожидания, если это необходимо
        self.wait = WebDriverWait(self.driver, wait_timeout)

    # Локаторы элементов страницы.
    username_input = "//input[@name='USER_LOGIN']"  # Локатор поля ввода логина.
    password_input = "//input[@type='password']"  # Локатор поля ввода пароля.
    login_button = "//span[@class = 'cabinet']"  # Локатор кнопки "Личный кабинет".
    submit_button = "//button[@class = 'btn btn-blue']"  # Локатор кнопки "Войти".
    login_title = "//*[@id='modal-login']/div/div/div/div/div[1]/div"  # Локатор заголовка окна регистрации.
    name_button_login = "//span[@class = 'name']"  # Локатор название кнопки личный кабинет.
    label_login = "//div[@class='form-email form-group']//label[contains(@class, 'form-label')]"  # Локатор название поля логин.

    label_pass = "//div[@class='form-pass form-group mb_15']//label[contains(@class, 'form-label')]"  # Локатор название поля пароль.
    button_add_card = "//button[@class ='to-cart-btn elem-to_cart']"  # Кнопка добавить в корзину.
    agree_button = "//a[@class = 'cookie-msg__button']"  # Кнопка "Согласен" модального окна.

    # Getters
    # def get_enter_username(self):   # Возвращает локатор поля ввода логина.
    #     return self.get_element(self.username_input)
    #
    # def get_enter_password(self):   # Возвращает локатор поля ввода пароля.
    #     return self.get_element(self.password_input)
    #
    # def get_login_button(self):     # Возвращает локатор кнопки "Личный кабинет"
    #     return self.get_element(self.login_button)
    #
    # def get_submit_button(self):    # Возвращает локатор кнопки "Войти"
    #     return self.get_element(self.submit_button)
    #
    # def get_login_title(self):
    #     return self.get_element(self.login_title)  # Возвращает заголовок окна авторизации/регистрации.
    #
    # def get_name_button_login(self):    # Возвращает локатор имя на кнопки "Личный кабинет"
    #     return self.get_element(self.name_button_login)

    # Actions (Действия)

    def click_login(self):  # Нажатие на кнопку "Личный кабинет"
        self.click_element(self.login_button)

    def input_user_name(self, user_name):
        self.input_in(self.username_input, user_name)

    def input_user_password(self, password):
        self.input_in(self.password_input, password)

    def click_submit_button(self):
        self.click_element(self.submit_button)

    # def

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.assert_url_2('https://sad-i-ogorod.ru/')  # Проверка ожидаемой url
        # self.click_button_modal()  # Клик на кнопку "Согласен" модального окна.
        self.click_login()  # Кликаем на кнопку "Личный кабинет"
        self.check_page_header(self.login_title, "Вход")  # Проверяем значение заголовка странице авторизации.
        self.input_user_name('testlessdns@gmail.com')
        self.input_user_password('zaqwsx123')
        self.get_text(self.label_login)  # Значение название поля Логин
        self.get_text(self.label_pass)  # Значение название поля Пароль
        self.click_submit_button()  # Клик на кнопку "Войти"
        self.assert_url_2('https://sad-i-ogorod.ru/?login=yes')  # Проверка ожидаемой URL
        self.get_text(self.name_button_login)  # Проверка название кнопки Личный кабинет.
        # self.value_element(self.name_button_login)  # Проверка имя на кнопки "Личный кабинет"

    # def add_products_to_cart(self):
