
class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    def open_order_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')




