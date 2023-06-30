from base.base_class import BasePage


class CardPage(BasePage):
    url = 'https://sad-i-ogorod.ru/cart/?login=yes'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


# Локаторы элементов страницы.
cart_header = "//div[@class='cart']/h1[text()='Корзина']"  # Заголовок станице Корзина
total_price_card = "//div[@class='bask-page__parcelTotal']/span[@class='bask-page__parcelTotal-price']"     # Итоговая сумма в корзине
