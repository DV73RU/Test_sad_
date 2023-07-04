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
