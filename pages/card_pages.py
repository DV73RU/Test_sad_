from base.base_class import BasePage


class CardPage(BasePage):
    url = 'https://sad-i-ogorod.ru/cart/?login=yes'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver