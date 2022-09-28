from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from pages.order import PersonalData, RentScooter, OrderConfirmationWindow, WindowOfCompletedOrder
from pages.base import BasePage



class TestOrderPage:

    driver = None

    @allure.title('Инициализируем драйвер')
    def setup(self):
        self.driver = webdriver.Firefox()

    @allure.testcase('Заказ самоката')
    @allure.description('Проверяем процесс первого заказа самоката с положительным сценарием')
    @allure.title('Заказ самоката')
    def test_order_first_client(self):
        base = BasePage(self.driver)
        base.open_order_page()
        order_page = PersonalData(self.driver)
        order_page.first_order('Кирилл', 'Тимофеев', 'Москва', '891569851272')

        scooter_page = RentScooter(self.driver)
        scooter_page.first_scooter('Как можно быстрее')

        order_confirmation = OrderConfirmationWindow(self.driver)
        order_confirmation.order_confirmation_first_client()

        order_completed = WindowOfCompletedOrder(self.driver)
        order_completed.completed_order_first_client()
        assert self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')


    @allure.testcase('Заказ самоката')
    @allure.description('Проверяем процесс второго заказа самоката с положительным сценарием')
    @allure.title('Заказ самоката')
    def test_order_second_client(self):
        base = BasePage(self.driver)
        base.open_order_page()
        order_page = PersonalData(self.driver)
        order_page.second_order('Виктория', 'Тимофеева', 'Москва', '89100000001')

        scooter_page = RentScooter(self.driver)
        scooter_page.second_scooter('Не торопитесь')

        order_confirmation = OrderConfirmationWindow(self.driver)
        order_confirmation.order_confirmation_second_client()

        order_completed = WindowOfCompletedOrder(self.driver)
        order_completed.completed_order_second_client()
        assert self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')


    @allure.title('Закрываем драйвер')
    def teardown(self):
        self.driver.quit()

