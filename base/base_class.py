import time

import pytest
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


class BasePage:
    TIMEOUT = 20  # Время ожидания доступности элемента.

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    """
    Метод перехода на URL
    """

    def go_to_url(self, url):
        return self.driver.get(url)

    """
    Метод видимости элемента
    """

    def is_element_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False

    """
    Метод возвращает локатор элемента.
    """

    def get_element(self, locator):  # Возвращает элемент
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return element
        except TimeoutException as e:
            raise NoSuchElementException(f"Элемент с локатором '{locator}' не найден {e}")


    """
    Метод проверки фактического заголовка странице с ожидаемым.
    header_locator - Значение спарсенного заголовок со странице.
    expected_header - Ожидаемое значение заголовка.
    """

    def check_page_header(self, header_locator, expected_header):  # Проверка заголовка странице
        # try:
        header_element = self.get_element(header_locator)
        header_text = header_element.text  # Фактический заголовок.
        assert header_text == expected_header, f"Ошибка: Заголовок страницы '{header_text}' не соответствует ожидаемому '{expected_header}'"
        print(f"Успех: Заголовок страницы '{header_text}' соответствует ожидаемому '{expected_header}'")
            # return True
        # except TimeoutException:
        #     pytest.fail("Ошибка: Заголовок страницы не найден или не видим!")
            # return False
        # except NoSuchElementException as e:
        #     pytest.fail(f"Ошибка: Элемент с локатором '{header_locator}' не найден на странице: {e}")
            # return None
        # except Exception as e:
        #     print(f"Ошибка: Неожиданная ошибка при проверке заголовка страницы: {e}")
        #     return None

    """
    Второй метод проверки url
    expected_url - Ожидаемое значение url
    current_url - Фактическое значение url
    """

    def assert_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL не соответствует ожидаемому: {expected_url}. Фактический: {current_url}!"
        print(f"Переход на ожидаемый url: {current_url}")

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
            pytest.fail(f"Элемент {value_button} с локатором: {locator} не найден! ")

    """
	Метод для проверки надписи на кнопке после авторизации.
    before_auth=True  - Если необходимо проверить текст после авторизации, можно явно указать
    """

    def get_button_text(self, button_locator, expected_text, before_auth=True):
        try:
            button_text = self.get_text(button_locator)  # Получаем текст кнопки
            if before_auth:
                assert button_text == expected_text, f"Ошибка! Текст кнопки до авторизации: {button_text}, ожидаемый текст: {expected_text}"
                print(f"Текст кнопки до авторизации соответствует ожидаемому: {button_text}.")
            else:
                assert button_text == expected_text, f"Ошибка! Текст кнопки после авторизации: {button_text}, ожидаемый текст: {expected_text}"
                print(f"Текст кнопки после авторизации соответствует ожидаемому: {button_text}.")
            # return True
        except TimeoutException:
            print("Ошибка: Текст кнопки не найден или не видим!")
            # return False
        except NoSuchElementException as e:
            print(f"Ошибка: Элемент с локатором '{button_locator}' не найден на странице: {e}")
            # return None

    """
    Метод проверки условия активной кнопки 'Оформить заказ'
    '"""

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
        return value_element

    """
    Метод ввода в поле ввода.
    """

    def input_in(self, input_locator, label_locator, value):
        try:
            element = self.get_element(input_locator)  # Поле ввода
            element.clear()  # Очистить поле ввода
            element.send_keys(value)  # Ввести значение в поле ввода

            # Получить название поля ввода из элемента label с помощью метода get_text
            field_name = self.get_text(label_locator)  # Получаем текст элемента label

            print(f"В поле '{field_name}' введено: {value}")
        except Exception as e:
            print(f"Ошибка при вводе текста в поле: {e}")

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

    def go_to_pages(self, url):
        self.driver.get(self.url)
        self.driver.maximize_window()

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
                                                               '').replace(' ', '') # Удаление лишних элементов в цене продукта.
            product_quantity = product.find_element(By.XPATH,
                                                    ".//td[@data-title='Количество']/div[@class='value']/div[@class='elem-counter']/input[@type='number']").get_attribute(
                "value")  # Локатор количества добавленного продукта.
            product_total_price_element = product.find_element(By.XPATH,
                                                               ".//td[@data-title='Стоимость']/span[@class='value nowrap']")  # Локатор общей стоимости продукта.
            product_total_price = product_total_price_element.text.replace('.00 i', '').replace(' ',
                                                                                                '')  # Удаление лишний
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
            print(f"В корзине присутствуют товары: ")
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

        order_total_price = order_total_price_element.text.replace(".00 i", "").replace(' ', '')    # Удаление пробела и лишних знаков после цены.
        print(f"Общая стоимость заказа (на странице): {order_total_price}")
        print(f"Общая стоимость заказа (рассчитанная): {total_order_price}")
        # print(type(order_total_price))
        # print(type(total_order_price))

        # Сравнить цены, если compare_prices=True
        if compare_prices:
            order_total_price = int(order_total_price)
            assert order_total_price == total_order_price, "Общая стоимость заказа не совпадает с расчётной стоимостью заказа."
            # pytest.fail("Общая стоимость заказа не совпадает с расчётной стоимостью заказа.")   # Пишем в консоль инфу о ошибке.
            print("Общая стоимость заказа совпадает c расчётной стоимостью заказа.")

            return products_list  # Возвращаем список товаров

    """
    Метод добавления товара в козину.
    max_cart_total=1000 - сумма по умолчанию добавления товара в корзину
    """

    def add_to_cart(self, max_cart_total=1000): #// TODO можно удалять этот метод

        # Найти все кнопки "Добавить в корзину"

        # cart_price = self.driver.find_element(By.XPATH,"//span[@class='price' or @class='no-product']")  # Локатор Суммы заказа в корзине

        add_to_card_buttons = self.driver.find_elements(By.XPATH, "//button[@class='to-cart-btn elem-to_cart']")

        # Проверить наличие товаров на странице
        if len(add_to_card_buttons) == 0:
            print("На странице нет товаров для добавления в корзину.")
            return

        # Кликнуть на каждую кнопку "Добавить в корзину"
        # Проверить доступность каждой кнопки "Добавить в корзину"
        for button in add_to_card_buttons:
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
                print(f"Кнопка 'Добавить в корзину' кликнута для товара: {product_name} : {product_price}")
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
    Добавление товара в корзину V.2.0
    Проверка название и цены у карточки товара с названием и ценой в Pop-up окне.
    Ограничения в сумме заказа.
    """

    def add_to_card2(self, max_card_total): #// TODO можно удалять этот метод
        max_card_total = 2000  # Здесь укажите нужное значение

        # Найти все кнопки "Добавить в корзину"

        add_to_card_buttons = self.driver.find_elements(By.XPATH, "//button[@class='to-cart-btn elem-to_cart']")

        # Проверить наличие товаров на странице
        if len(add_to_card_buttons) == 0:
            print("На странице нет товаров для добавления в корзину.")
            return

        # Кликнуть на каждую кнопку "Добавить в корзину"
        # Проверить доступность каждой кнопки "Добавить в корзину"
        for button in add_to_card_buttons:
            if not button.is_enabled():
                print("Кнопка 'Добавить в корзину' недоступна")
                continue

            # Получить информацию о товаре из кнопки "Добавить в корзину" до нажатия
            parent_element = button.find_element(By.XPATH,
                                                 ".//ancestor::form[@class='info-wrapper add-bask-form-list ']")

            product_name = parent_element.find_element(By.XPATH,
                                                       ".//a[@class='prod-name js-prod-link-list']").get_attribute(
                "data-name")
            product_price_element = parent_element.find_element(By.XPATH, ".//div[@class='prod-price ']")
            product_price = float(product_price_element.text.replace('.00 i', '').replace(' ', ''))

            # Скрыть элемент, перекрывающий кнопку, с помощью JavaScript (Pop-up окно Согласие на работу с куками)

            self.driver.execute_script("arguments[0].style.visibility='hidden';", button)
            print("Закрыто окно 'Работа с куками'")

            # Выполнить клик с помощью JavaScript
            self.driver.execute_script("arguments[0].click();", button)

            # Ограничить сумму в корзине до 800 (переменная max_cart_total)
            time.sleep(5)

            try:
                # # Выполнить клик с помощью JavaScript
                self.driver.execute_script("arguments[0].click();", button)
                print("Кнопка 'Добавить в корзину' кликнута для товара:", product_name, product_price)
                # Дождаться появления Pop-up окна
                pop_up_element = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='box-cart-popup js-added-product']"))
                )
                # Получить все элементы <a> с классом "c_link" внутри Pop-up окна
                products_in_pop_up = pop_up_element.find_elements(By.XPATH, ".//a[@class='c_link']")

                # Найти совпадение для добавленного товара по имени и цене
                found_match = False
                for product in products_in_pop_up:
                    product_name_in_pop_up = product.find_element(By.XPATH, ".//span[@class='name']").text
                    product_price_in_pop_up = int(
                        product.find_element(By.XPATH, ".//span[@class='c_price']").text.replace('.00 i', ''))

                    print(f"Название в Pop-up: {product_name_in_pop_up}, цена: {product_price_in_pop_up}")
                    if product_name_in_pop_up == product_name:
                        if product_name_in_pop_up == product_name and product_price_in_pop_up == product_price:
                            print(
                                "Информация о товаре в Pop-up окне соответствует информации о товаре, добавленном в корзину.")
                            found_match = True
                            break

                        else:
                            print(
                                "Информация о товаре в Pop-up окне не соответствует цене товара, добавленного в корзину.")
                            found_match = True
                            break

                if not found_match:
                    print(
                        "Ошибка! Информация о товаре в Pop-up окне не соответствует информации о товаре, добавленном в корзину.")

                # Дождаться закрытия Pop-up окна
                WebDriverWait(self.driver, 15).until(
                    EC.invisibility_of_element_located((By.XPATH, "//div[@class='box-cart-popup js-added-product']"))
                )
                print("Pop-up окно закрыто для товара:", product_name)

                # Обновить видимость элемента после клика
                self.driver.execute_script("arguments[0].style.visibility='visible';", button)

                # Добавить небольшую паузу перед следующим кликом
                time.sleep(5)

                # Обновить сумму заказа в корзине и проверить ограничение по максимальной сумме
                cart_total_element = self.driver.find_element(By.XPATH, "//span[@class='price']")
                cart_total_text = cart_total_element.text
                cart_price_value = int(cart_total_text.replace('.00 i', '').replace(' ', ''))

                if cart_price_value > max_card_total:
                    print(f"Общая сумма заказа превышает {max_card_total}, добавление товаров в корзину остановлено")
                    print(f"Товары успешно добавлены в корзину на сумму: {cart_price_value}")
                    return

            except TimeoutException:
                print("Pop-up окно не появилось или не закрылось для товара:", product_name)

    def add_to_card3(self, max_card_total, button_add_to_card_locator, info_wrapper_locator, product_name_locator, product_price_locator):
        # Найти все кнопки "Добавить в корзину"
        add_to_card_buttons = self.driver.find_elements(By.XPATH, button_add_to_card_locator)

        # Проверить наличие товаров на странице
        if len(add_to_card_buttons) == 0:
            print("На странице нет товаров для добавления в корзину.")
            return

        for button in add_to_card_buttons:
            if not button.is_enabled():
                print("Кнопка 'Добавить в корзину' недоступна")
                continue

            # Получить информацию о товаре из кнопки "Добавить в корзину" до нажатия
            parent_element = button.find_element(By.XPATH, info_wrapper_locator)

            product_name = parent_element.find_element(By.XPATH, product_name_locator).get_attribute("data-name")
            product_price_element = parent_element.find_element(By.XPATH, product_price_locator)
            product_price = int(product_price_element.text.replace('.00 i', '').replace(' ', ''))

            # Скрыть элемент, перекрывающий кнопку, с помощью JavaScript (Pop-up окно Согласие на работу с куками)
            self.driver.execute_script("arguments[0].style.visibility='hidden';", button)
            print("Закрыто окно 'Работа с куками'")

            # Выполнить клик с помощью JavaScript
            self.driver.execute_script("arguments[0].click();", button)

            # Ограничить сумму в корзине до 800 (переменная max_cart_total)
            time.sleep(5)

            try:
                self.driver.execute_script("arguments[0].click();", button)
                print("Кнопка 'Добавить в корзину' кликнута для товара:", product_name, product_price)

                # Дождаться появления Pop-up окна
                pop_up_element = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='box-cart-popup js-added-product']"))
                )
                # Получить все элементы <a> с классом "c_link" внутри Pop-up окна
                products_in_pop_up = pop_up_element.find_elements(By.XPATH, ".//a[@class='c_link']")

                # Найти совпадение для добавленного товара по имени и цене
                found_match = False
                for product in products_in_pop_up:
                    product_name_in_pop_up = product.find_element(By.XPATH, ".//span[@class='name']").text
                    # Когда не возвращает цену из POP-UP окна (не разобрался с причиной)
                    try:
                        product_price_in_pop_up = int(product.find_element(By.XPATH, ".//span[@class='c_price']").text.replace('.00 ', '').replace('i', ''))
                    except ValueError:
                        print("Ошибка: невозможно преобразовать цену товара в число")
                        continue

                    print(f"Название в Pop-up: {product_name_in_pop_up}, цена: {product_price_in_pop_up}")
                    if product_name_in_pop_up == product_name:
                        if product_name_in_pop_up == product_name and product_price_in_pop_up == product_price:
                            print(
                                "Информация о товаре в Pop-up окне соответствует информации о товаре, добавленном в корзину.")
                            found_match = True
                            break

                        else:
                            print(
                                "Информация о товаре в Pop-up окне не соответствует цене товара, добавленного в корзину.")
                            found_match = True
                            break

                if not found_match:
                    print(
                        "Ошибка! Информация о товаре в Pop-up окне не соответствует информации о товаре, добавленном в корзину.")

                # Дождаться закрытия Pop-up окна
                WebDriverWait(self.driver, 15).until(
                    EC.invisibility_of_element_located((By.XPATH, "//div[@class='box-cart-popup js-added-product']"))
                )
                print("Pop-up окно закрыто для товара:", product_name)

                # Обновить видимость элемента после клика
                self.driver.execute_script("arguments[0].style.visibility='visible';", button)

                # Добавить небольшую паузу перед следующим кликом
                time.sleep(5)

                # Обновить сумму заказа в корзине и проверить ограничение по максимальной сумме
                cart_total_element = self.driver.find_element(By.XPATH, "//span[@class='price']")
                cart_total_text = cart_total_element.text
                cart_price_value = int(cart_total_text.replace('.00 i', '').replace(' ', ''))

                # Если сумма в корзине + цена товара больше max_card_total, то остановить добавление в корзину
                if cart_price_value + product_price > max_card_total:
                    print(f"Следующие добавление товара в корзину превысит {max_card_total}, добавление товаров в корзину остановлено")
                    print(f"Товары успешно добавлены в корзину на сумму: {cart_price_value}")
                    return

            except TimeoutException:
                print("Pop-up окно не появилось или не закрылось для товара:", product_name)

    # Пример использования:


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
    Метод проверки функциональности ограничения суммы заказа
    min_total - минимальная сумма заказа 
    value_free_delivery - Сумма бесплатной доставки

    """
    def check_order_total_2(self):  # TODO использовать написанные методы для поиска локаторов, что бы выводить мессеги о не найденном локторе
        # Получаем элемент, содержащий информацию о стоимости заказа
        total_element = self.driver.find_element(By.XPATH, "//span[@class='bask-page__parcelTotal-price']")  # Локатор суммы заказа

        # Получаем текст элемента суммы заказа
        total_element = total_element.text
        order_total = total_element.split(":")[1]   # Делим текст на список разделённым ':', берем 2 элем.(цену) списка
        value_order_total = int(order_total.replace('.00 i', '').replace(' ', ''))  # Удаляем всё лишнее из цены.
        # print(value_order_total, type(value_order_total))

        # Проверяем условия и выполняем соответствующие действия
        if value_order_total <= 800:
            print("Проверка бизнес логике: Заказ меньше 800\n==========================================")
            # Проверяем отображение текста "Минимальная стоимость посылки 800.0"
            label_min_element = self.driver.find_element(By.XPATH,
                                                 "//div[@class='bask-page__parcelTotal-minPriceError']/span")  # Локатор текста мимимального заказа
            label_min_element = label_min_element.text.replace(' i', '')    # Удаляем лишние элементы из текста

            assert f"Минимальная стоимость посылки 800.0" in label_min_element  # Проверяем присутствие текста в найденном label
            print(f"На странице присутствует ожидаемый текст: {label_min_element}")

            # Проверяем кликабельность кнопки "Перейти в каталог семян"
            catalog_button = self.driver.find_element(By.XPATH,
                                                      "//a[contains(text(), 'Перейти в каталог семян')]")   # Локатор кнопки "Перейти в каталог семян"
            assert catalog_button.is_enabled()
            print("Кнопка 'Перейти в каталог семя' кликабельна")

            try:
                self.driver.find_element(By.XPATH, "//form[@action='order/']")  # Локатор активности кнопки
                print("Кнопка 'Оформить заказ' кликабельна")
            except NoSuchElementException:  # Если локатор не найден, то кнопка не кликабельна
                print("Кнопка 'Оформить заказ' не кликабельна\nНе доступен переход на страницу 'Оформить заказ'")
                pytest.skip()  # Пропускаем остальные части теста

        elif 800 < value_order_total < 2000:
            print("Проверка бизнес логике: Заказ больше 800 и меньше 2000\n==========================================")

            # Проверяем кликабельность кнопки "Оформить заказ"
            order_button = self.driver.find_element(By.XPATH, "//button[@class = 'bask-page__orderTotal-btn']")
            assert order_button.is_enabled()
            print(f"Кнопка 'Оформить заказ' кликабельна")

        elif value_order_total >= 2000:
            print("Проверка бизнес логике: Заказ больше или равен 2000\n=========================================")
            ship_element = self.driver.find_element(By.XPATH,
                                                     "//span[@class='bask-page__parcelTotal-freeship']")  # Локатор текста бесплатная доставка
            # Проверяем отображение текста "Бесплатная доставка"
            assert "Бесплатная доставка" in ship_element.text
            print(f"На странице присутствует ожидаемый текст: {ship_element.text}")

            # Проверяем кликабельность кнопки "Оформить заказ"
            order_button = self.driver.find_element(By.XPATH, "//button[@class = 'bask-page__orderTotal-btn']")
            assert order_button.is_enabled()
            print(f"Кнопка 'Оформить заказ' кликабельна")

    """
    Чекаем сумму возможную для продолжения заказа
	"""

    def check_order_total(self, locator_min_price):
        min_price_element = self.driver.find_element(By.XPATH, locator_min_price)
        min_price_text = min_price_element.text
        min_price = int(min_price_text.replace('.00 i', ''))

        return min_price

    def order_logic(self, order_amount):

        if order_amount < 800:
            # Ожидание текста "Минимальная стоимость заказа 800.0 р"
            min_price_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='bask-page__parcelTotal-minPrice']"))
            )
            assert min_price_text.text == "Минимальная стоимость заказа 800.0 р"

            # Ожидание неактивной кнопки "Оформить заказ"
            order_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//button[@class='bask-page__orderTotal-btn bask-page__orderTotal-btn--disable']"))
            )
            assert not order_button.is_enabled()

        else:
            # Ожидание исчезновения текста "Минимальная стоимость заказа 800.0 р"
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((By.XPATH, "//span[@class='bask-page__parcelTotal-minPrice']"))
            )

            # Ожидание появления текста "Бесплатная доставка от 2000 р."
            free_shipping_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='bask-page__parcelTotal-freeship']"))
            )
            assert free_shipping_text.text == "Бесплатная доставка от 2000 р."

            # Ожидание активной кнопки "Оформить заказ"
            order_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@class='bask-page__orderTotal-btn']"))
            )
            assert order_button.is_enabled()

    """
    Метод закрытия окна работа с куками
    """

    def close_cookie_banner(self):  # продолжить работу даже в том случае, если элемент не найден.
        try:
            cookie_banner = self.driver.find_element(By.CLASS_NAME, "cookie-msg__wrapper")
            if cookie_banner.is_displayed():
                try:
                    # Закрыть баннер согласия на использование файлов cookie, если элемент cookie-msg__close найден
                    cookie_banner.find_element(By.XPATH, "//a[@class='cookie-msg__button']").click()
                    print("Закрыт банер работы с куками")
                except NoSuchElementException:
                    pass  # Если элемент cookie-msg__close не найден, проигнорировать ошибку
        except NoSuchElementException:
            pass  # Баннер с согласием на использование файлов cookie отсутствует или не виден, поэтому мы игнорируем исключение

    """
    Метод клика на radio button
    """

    def click_radio_2(self, locator):
        try:
            radio_button_registered = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locator))  # // TODO использовать универсальный локатаор ID
            )
            button_text = self.get_text(locator)
            time.sleep(2)
            radio_button_registered.click()
            print(f"Кнопка '{button_text}' кликнута.")
        except NoSuchElementException:
            print(f"Кнопка c локатором: {locator} не найдена.")

    """
    Метод клика на radio button с помощью JavaScript
    
    """

    def click_radio(self, locator):
        try:
            radio_button_registered = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
            self.driver.execute_script("arguments[0].click();", radio_button_registered)
            print(f"Кликнута radio button '{self.get_text(locator)}'.")  # // TODO Забрать название метки из локатора
        except NoSuchElementException:
            pytest.fail(f"radio button '{locator}' не найдена.")

    """
    +=====================================================+
    |  Метод проверки введённых значений в поля ввода     |
    |  input_locator - Локатор поля ввода                 |
    |  label_locator - Локатор метки поля ввода           |
    |  expected_value - Проверяемое значение в поле ввода |
    ======================================================+
    """

    def check_input_value_2(self, input_locator, label_locator, expected_value):
        try:
            input_element = self.get_element(input_locator)  # Находим элемент поля ввода
            actual_value = input_element.get_attribute("value")  # Получаем значение поля ввода

            # Получаем текст метки с помощью метода get_text, передавая локатор метки
            label_text = self.get_text(label_locator)

            # Проверяем, соответствует ли введенное значение ожидаемому
            assert actual_value == expected_value, f"Значение поля '{label_text}' не соответствует ожидаемому: {expected_value}"
            print(f"Значение поля '{label_text}' соответствует ожидаемому: {expected_value}")
        except NoSuchElementException:
            pytest.fail(f"Поле не найдено: {input_locator}.")
