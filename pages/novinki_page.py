"""
Класс странице Новинки
"""
from selenium import webdriver

from base.base_class import BasePage


driver = webdriver.Chrome()


class NovinkiPage(BasePage):
    url = 'https://sad-i-ogorod.ru/catalog/novinki.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# novinki_page = NovinkiPage(driver)
# novinki_page.go_to_page()
#
# # Добавление товаров в корзину
# novinki_page.add_products_to_cart()