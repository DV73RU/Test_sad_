import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

""" 
Класс BasePage служит в качестве базового класса, который содержит 
общие методы и функциональность.
"""

""" v.3
Функция удаляет всё лишние элементы от цены товара
"""


def process_total_price(price_text):
    price_text = price_text.strip().replace(' ', '')  # Удаляем пробелы и лишние символы из начала и конца строки
    price_text = price_text.replace(',', '.')  # Заменяем запятую на точку
    price_text = price_text[:-1]  # Удаляем последний символ 'i'
    return float(price_text)
    # return float(processed_price)


class BasePage():
    TIMEOUT = 30  # Время ожидания доступности элемента.

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    """Метод возвращает локатор элемента."""

    def get_element(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
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
        value_button = None
        try:
            element = self.get_element(locator)
            value_button = element.text  # Забираем название элемента.
            element.click()
            print(f"Нажата кнопка: {value_button}")
        except NoSuchElementException:
            print(f"Элемент {value_button} с локатором: {locator} не найден! ")

    """Метод проверки условия активной кнопки 'Оформить заказ'"""

    # // TODO Перенести метод в cared_pages.py
    def click_checkout(self, button_order, button_order_not, locator_min_price):
        order_total = 0  # Инициализация order_total перед блоком try
        try:
            element_active = self.get_element(button_order)
            value_button = element_active.text  # Забираем название элемента.
            order_total = self.check_order_total(locator_min_price)

            if order_total < 800:
                print(f"Кнопка {value_button} не активна, так как сумма заказа: {order_total} меньше 800.")
            else:
                element_active.click()
                print(f"Нажата активная кнопка: {value_button}")
                if order_total < 800:
                    print(f"Сумма заказа {order_total} меньше 800, но кнопка всё равно активна.")
        except NoSuchElementException:
            try:
                element_inactive = self.get_element(button_order_not)
                value_button = element_inactive.text
                order_total = self.check_order_total(locator_min_price)  # Обновление order_total
                print(f"Кнопка {value_button} не активна, сумма заказа: {order_total} меньше 800.")
            except NoSuchElementException:
                print(f"Не удалось найти кнопку оформления заказа на странице.")

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
    Метод перехода на страницу.
    """

    def go_to_pages(self, url, locator):
        self.driver.get(url)
        self.driver.maximize_window()
        self.click_element(locator)  # Кликаем на кнопку перехода на страницу
        # self.assert_url_2(url)  # Проверка ожидаемой url странице

    """
    Метод парсинга товаров на странице каталога
    show_list=False - Параметр скрывает список спарсенных товаров.
    """

    def parse_product(self, locator, show_list=True):  # локатор карточки товара.
        products = self.driver.find_elements(By.XPATH, locator)
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

        if show_list:
            # Вывести список товаров
            # Цикл обходит по каждому элемента и извлекаем данные о товаре.
            print(f"Список товаров на странице: ")
            for product_info in products_list:
                product_number = product_info['№']
                product_name = product_info['Название']
                product_price = product_info['Цена']

                print(f"№:{product_number}, Название:{product_name}, Цена:{product_price}")

            # Вывести количество найденных товаров
            total_products = len(products_list)
            print(f"Количество найденных товаров на странице :{total_products}")

    """
    Метод проверка иконки корзины на наличие в ней суммы товаров
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
            total_price = price_elements[0].text.replace('.00 i',
                                                         '')  # Избавляемся от лишних элементов в значение цены.
            print(f"Сумма добавленного товара в корзине: {total_price}")
        else:
            print("В корзине нет товаров.")

    """
    Метод парсинга товаров на странице корзины.
    Сравнение суммы покупки на странице корзины с расчётной.
    Опции: print_products=False - Не выводить спарсенный список товаров
            compare_prices=False - Не выводить сравнение цен на странице и расчётные.
    """

    def parse_products_card(self, locator, print_products=True, compare_prices=True):
        # Находим все товары на странице
        products = self.driver.find_elements(By.XPATH, locator)

        # Создаем список для хранения информации о товарах
        products_list = []

        # Инициализируем переменную для общей стоимости заказа
        total_order_price = 0

        # Проходимся по каждому товару и извлекаем информацию
        for product in products:
            # Получаем информацию о товаре
            product_name = product.find_element(By.XPATH, ".//td/a").text  # Локатор название продукта.
            product_price_element = product.find_element(By.XPATH,
                                                         ".//td[@data-title='Цена']/span[@class='value nowrap']")  # Локатор цены продукта
            product_price = product_price_element.text.replace('.00 i',
                                                               '')  # Удаление лишних элементов в цене продукта.
            product_quantity = product.find_element(By.XPATH,
                                                    ".//td[@data-title='Количество']/div[@class='value']/div[@class='elem-counter']/input[@type='number']").get_attribute(
                "value")  # Локатор количества добавленного продукта.
            product_total_price_element = product.find_element(By.XPATH,
                                                               ".//td[@data-title='Стоимость']/span[@class='value nowrap']")  # Локатор общей стоимости продукта.
            product_total_price = product_total_price_element.text.replace('.00 i', '')  # Удаление лишний
            # элементов из цены продукта.

            # Добавляем цену товара к общей стоимости заказа
            total_order_price += int(product_total_price)

            # Создаем словарь с информацией о товаре
            product_info = {
                "Название": product_name,
                "Цена": product_price,
                "Количество": product_quantity,
                "Стоимость": product_total_price
            }

            # Добавляем словарь в список товаров
            products_list.append(product_info)

        # Вывести список товаров, если print_products=True
        if print_products:
            for product_info in products_list:
                product_name = product_info['Название']
                product_price = product_info['Цена']
                product_quantity = product_info['Количество']
                product_total_price = product_info['Стоимость']

                print(
                    f"Название: {product_name}, Цена: {product_price}, Количество: {product_quantity}, Стоимость: {product_total_price}")

        # Выводим общую стоимость заказа
        order_total_price_element = self.driver.find_element(By.XPATH,
                                                             "//span[@class='bask-page__orderTotal-price']/span")  # Локатор общей суммы заказа
        order_total_price = order_total_price_element.text.replace(" ", "", 1).replace(".00 i",
                                                                                       "")  # Удаление пробела и лишних знаков после цены.
        print(f"Общая стоимость заказа (на странице): {order_total_price}")
        print(f"Общая стоимость заказа (рассчитанная): {total_order_price}")

        # Сравнить цены, если compare_prices=True
        if compare_prices:
            order_total_price = int(order_total_price)  # Из строки в число.
            if order_total_price == total_order_price:
                print("Общая стоимость заказа совпадает c расчётной стоимостью заказа.")
            else:
                print("Общая стоимость заказа не совпадает с расчётной стоимостью заказа.")

        return products_list  # Возвращаем список товаров

    """
    Метод добавления товара в козину.
    max_cart_total=1000 - сумма по умолчанию добавления товара в корзину
    """

    def add_to_cart(self, max_cart_total=1000):

        # Найти все кнопки "Добавить в корзину"

        global cart_price_value
        # cart_price = self.driver.find_element(By.XPATH,
        #                                       "//span[@class='price' or @class='no-product']")  # Локатор Суммы заказа в корзине

        add_to_cart_buttons = self.driver.find_elements(By.XPATH, "//button[@class='to-cart-btn elem-to_cart']")

        # Проверить наличие товаров на странице
        if len(add_to_cart_buttons) == 0:
            print("На странице нет товаров для добавления в корзину.")
            return

        # Кликнуть на каждую кнопку "Добавить в корзину"
        # Проверить доступность каждой кнопки "Добавить в корзину"
        for button in add_to_cart_buttons:
            if not button.is_enabled():
                print("Кнопка 'Добавить в корзину' недоступна")
                continue
            # Найти родительский элемент кнопки "Добавить в корзину"
            parent_element = button.find_element(By.XPATH,
                                                 ".//ancestor::form[@class='info-wrapper add-bask-form-list ']")

            # Получить информацию о товаре из родительского элемента
            product_name = parent_element.find_element(By.XPATH,
                                                       ".//a[@class='prod-name js-prod-link-list']").get_attribute(
                "data-name")
            product_price_element = parent_element.find_element(By.XPATH, ".//div[@class='prod-price ']")
            product_price = product_price_element.text.replace('.00 i',
                                                               '')  # Избавляемся от лишних элементов в значение цены.

            # Скрыть элемент, перекрывающий кнопку, с помощью JavaScript
            # Pop-up окно Согласие на работу с куками
            self.driver.execute_script("arguments[0].style.visibility='hidden';", button)
            print("Закрыто окно 'Работа с куками'")

            # Выполнить клик с помощью JavaScript
            # self.driver.execute_script("arguments[0].click();", button)

            # Ограничить сумму в корзине до 800

            time.sleep(5)

            try:
                # # Выполнить клик с помощью JavaScript
                self.driver.execute_script("arguments[0].click();", button)
                print("Кнопка 'Добавить в корзину' кликнута для товара:", product_name, product_price)
                # Дождаться появления pop-up окна
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='box-cart-popup js-added-product']")))
                print("Pop-up окно открыто для товара:", product_name)

                # Дождаться закрытия pop-up окна
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located(
                        (By.XPATH, "//div[@class='box-cart-popup js-added-product']")))
                print("Pop-up окно закрыто для товара:", product_name)

                cart_total_element = self.driver.find_element(By.XPATH,
                                                              "//span[@class='price']")  # Локатор Суммы заказа в корзине
                cart_total_text = cart_total_element.text
                cart_price_value = int(cart_total_text.replace('.00 i', '').replace(' ', ''))

                if cart_price_value > max_cart_total:  # Прекращение добавление товара в корзину до суммы заказа.
                    print(f"Общая сумма заказа превышает {max_cart_total}, добавление товаров в корзину остановлено")
                    print(f"Товары успешно добавлены в корзину на сумму: {cart_price_value}")
                    return

            except TimeoutException:
                print("Pop-up окно не появилось или не закрылось для товара:", product_name)

            # Восстановить видимость элемента после клика
            # self.driver.execute_script("arguments[0].style.visibility='visible';", button)

            # Добавить небольшую паузу перед следующим кликом
            time.sleep(1)

    """
    Скролим до элемента
    """

    def scroll_pages_to_element(self, locator):
        try:
            action = ActionChains(self.driver)
            element = self.driver.find_element(locator)
            action.move_to_element(locator).perform()
            print(f"Скрол до элемента: {locator}")
        except NoSuchElementException:
            print(f"Элемент с локатором: {locator} не найден! ")

    """
    Чекаем сумму возможную для продолжения заказа
	"""

    def check_order_total(self, locator_min_price):
        min_price_element = self.driver.find_element(By.XPATH, locator_min_price)
        min_price_text = min_price_element.text
        min_price = int(min_price_text.replace('.00 i', ''))

        return min_price
