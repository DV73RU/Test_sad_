# product_page.py
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import BasePage

"""
Клаcс карточки товара на странице.
"""


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы карточки товара на странице
    info_wrapper = ".//ancestor::form[@class='info-wrapper add-bask-form-list ']"  # Локатор карточки товара
    button_add_to_card = "//button[@class ='to-cart-btn elem-to_cart']"# Локатор Кнопки добавить в корзину
    product_name = ".//a[@class='prod-name js-prod-link-list']"   # Локатор название товара
    product_price = ".//div[@class='prod-price ']"  # Локатор цены товара
    product_img = ""    # Локатор картинки товара
    favorite = ""  # Локатор кнопки "Добавить в избранное"
    counter = ""    # Локатор спинбокс
    control_minus = ""  # Локатор кнопки '-'
    control_plus = ""   # Локатор кнопки '+'

