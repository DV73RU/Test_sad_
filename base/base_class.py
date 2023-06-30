import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

""" Класс BasePage служит в качестве базового класса, который содержит 
общие методы и функциональность.
"""

"""Функция удаляет всё лишние элементы от цены товара"""


def process_total_price(price_text):
    price_text = price_text.strip().replace(' ', '')  # Удаляем пробелы и лишние символы из начала и конца строки
    price_text = price_text.replace(',', '.')  # Заменяем запятую на точку
    price_text = price_text[:-1]  # Удаляем последний символ 'i'
    return float(price_text)
    # return float(processed_price)


class BasePage():
    TIMEOUT = 20  # Время ожидания доступности элемента.

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    """Метод возвращает локатор элемента."""

    def get_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Элемент не найден: {locator}!")

    def get_url(self):
        return self.driver.current_url

    """
    Метод проверки фактического заголовка странице с ожидаемым.
    header_locator - Значение спарсенного заголовок со странице.
    expected_header - Ожидаемое значение заголовка.
    """

    def check_page_header(self, header_locator, expected_header):
        try:
            # wait = WebDriverWait(driver, 10)
            header_element = self.get_element(header_locator)
            header_text = header_element.text  # Фактический заголовок.
            if header_text == expected_header:  # Сравнение с ожидаемым.
                print(f"Заголовок страницы '{header_text}' успешно отображается")
            else:
                print(f"Заголовок страницы '{header_text}' не соответствует ожидаемому {expected_header}!")
        except TimeoutException:
            print("Заголовок страницы не найден или не видим!")

    """
    Не используется
    """

    def check_page_title(self, expected_title):
        try:
            self.wait.until(EC.visibility_of_element_located(expected_title))
            print(f"Заголовок страницы '{expected_title}' успешно отображается")
            return True
        except TimeoutException:
            print(f"Заголовок страницы '{expected_title}' не найден или не соответствует ожидаемому!")
            return False

    """Метод проверки url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"Good value url: {get_url}")

    """
    Второй метод проверки url
    expected_url - Ожидаемое значение url
    current_url - Фактическое значение url
    """

    def assert_url_2(self, expected_url):
        current_url = self.driver.current_url
        if current_url == expected_url:
            print(f"Переход на ожидаемый url: {current_url}")
        else:
            print(f"URL не соответствует ожидаемому: {expected_url}. Фактический: {current_url}!")

    """
    Метод нажатия на элемент.
    """

    # // TODO Написать сравнение ожидаемых названий и фактических.
    def click_element(self, locator):
        try:
            element = self.get_element(locator)
            value_button = element.text  # Забираем название элемента.
            element.click()
            print(f"Нажата кнопка: {value_button}")
        except NoSuchElementException:
            print(f"Элемент с локатором: {locator} не найден! ")

    """
    Метод возврата текста элемента.
    """

    def get_text(self, locator):
        element = self.get_element(locator)
        value_element = element.text
        print(value_element)
        return value_element

    """
    Метод ввода в поле ввода.
    """

    # // TODO Написать вывод название поля ввода.
    def input_in(self, locator, value):
        element = self.get_element(locator)  # Поле ввода
        element.clear()  # Очистить поле ввода
        element.send_keys(value)  # Ввести значение в поле ввода
        print(f"В поле ввода введено: {value}")

    """
    Метод клик на элемент. 
    Используя обход перекрытия всплывающим окном 'Мы используем cookie-файлы' 
    """

    def click_element_with_move_to(self, locator):
        element = self.get_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

        # Закрытие модального окна, если оно присутствует
        modal_window_locator = "//div[@class='cookie-msg']"
        modal_window = self.get_element(modal_window_locator)
        if modal_window:
            agree_button_locator = "//a[@class='cookie-msg__button']"
            agree_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, agree_button_locator))
            )
            agree_button.click()

    """
    Функция проверки иконки корзина на присутствие там суммы заказа.
    """
    def is_cart_empty(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='no-product']")))  # Локатор пустой корзины
            return True
        except TimeoutException:
            return False

    """
    Метод парсинга товаров на странице каталога.
    """
    def parsing_product(self):
        products = self.driver.find_elements(By.XPATH, "//a[@class='prod-name js-prod-link-list']")
        if len(products) == 0:
            print("На странице нет товаров.")
            return
        # Создать список для товаров
        products_list = []

        # Получить информацию о каждом товаре и добавить в список
        for product in products:
            # Получить номер товара
            product_number = product.get_attribute("data-id")

            # Получить название товара
            product_name = product.text

            # Получить цену товара
            product_price = product.get_attribute("data-price")

            # Создать словарь с информацией о товаре
            product_info = {
                "№": product_number,
                "Название": product_name,
                "Цена": product_price
            }

            # Добавить словарь в список товаров
            products_list.append(product_info)

        # Вывести список товаров
        # Цикл обходит по каждому элемента и извлекаем данные о товаре.
        for product_info in products_list:
            product_number = product_info['№']
            product_name = product_info['Название']
            product_price = product_info['Цена']

            print(f"№:{product_number}, Название:{product_name}, Цена:{product_price}")

    """
    Метод проверки корзины на наличие в ней товаров
    """
    def check_cart(self):
        # Проверка наличия пустой корзины
        empty_cart_elements = self.driver.find_elements(By.XPATH, "//span[@class='no-product']")
        if empty_cart_elements:
            print("Корзина пуста.")
            return

        # Проверка наличия товаров и получение суммы в корзине
        price_elements = self.driver.find_elements(By.XPATH, "//span[@class='price']")
        if price_elements:
            total_price = price_elements[0].text.replace('.00 i', '')   # Избавляемся от лишних элементов в значение цены.
            print(f"Сумма добавленного товара в корзине: {total_price}")
        else:
            print("В корзине нет товаров.")

    """
    Метод добавления товара в корзину
    """

    def add_to_cart(self):
        # Найти все кнопки "Добавить в корзину"
        add_to_cart_buttons = self.driver.find_elements(By.XPATH, "//button[@class='to-cart-btn elem-to_cart']")

        # Проверить наличие товаров на странице
        if len(add_to_cart_buttons) == 0:
            print("На странице нет товаров для добавления в корзину.")
            return

        # Кликнуть на каждую кнопку "Добавить в корзину"
        for button in add_to_cart_buttons:
            # Найти родительский элемент кнопки "Добавить в корзину"
            parent_element = button.find_element(By.XPATH, ".//ancestor::form[@class='info-wrapper add-bask-form-list ']")

            # Получить информацию о товаре из родительского элемента
            product_name = parent_element.find_element(By.XPATH, ".//a[@class='prod-name js-prod-link-list']").get_attribute("data-name")
            product_price_element = parent_element.find_element(By.XPATH, ".//div[@class='prod-price ']")
            product_price = product_price_element.text.replace('.00 i', '')     # Избавляемся от лишних элементов в значение цены.

            # Скрыть элемент, перекрывающий кнопку, с помощью JavaScript
            # Pop-up окно Согласие на работу с куками
            self.driver.execute_script("arguments[0].style.visibility='hidden';", button)

            # Выполнить клик с помощью ActionChains
            # actions = ActionChains(self.driver)
            # actions.move_to_element(button).click().perform()

            try:
                # Выполнить клик с помощью JavaScript
                self.driver.execute_script("arguments[0].click();", button)

                # Дождаться появления pop-up окна
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='box-cart-popup js-added-product']")))
                print("Pop-up окно открыто для товара:", product_name)

                # Дождаться закрытия pop-up окна
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.XPATH, "//div[@class='box-cart-popup js-added-product']")))
                print("Pop-up окно закрыто для товара:", product_name)

                print("Кнопка 'Добавить в корзину' кликнута для товара:", product_name, product_price)

            except TimeoutException:
                print("Pop-up окно не появилось или не закрылось для товара:", product_name)

            # Восстановить видимость элемента после клика
            # self.driver.execute_script("arguments[0].style.visibility='visible';", button)

            # Добавить небольшую паузу перед следующим кликом
            time.sleep(1)

        print("Товары успешно добавлены в корзину.")