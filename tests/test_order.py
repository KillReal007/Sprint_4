from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure
from pages.home import HomePage
from pages.order import PersonalData, RentScooter, OrderConfirmationWindow, WindowOfCompletedOrder


class TestOrder:

    driver = None

    @allure.title('Инициализируем драйвер')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.testcase('Заказ самоката')
    @allure.description('Проверяем процесс первого заказа самоката с положительным сценарием')
    @allure.title('Заказ самоката')
    def test_order_first_client(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        order_page = PersonalData(self.driver)
        order_page.first_order('Кирилл', 'Тимофеев', 'Москва', '891569851272')

        scooter_page = RentScooter(self.driver)
        scooter_page.first_scooter('Как можно быстрее')

        order_confirmation = OrderConfirmationWindow(self.driver)
        order_confirmation.order_confirmation_first_client()

        order_completed = WindowOfCompletedOrder(self.driver)
        order_completed.completed_order_first_client()
        assert self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')

    @allure.title('Закрываем драйвер')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Инициализируем драйвер')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.testcase('Заказ самоката')
    @allure.description('Проверяем процесс второго заказа самоката с положительным сценарием')
    @allure.title('Заказ самоката')
    def test_order_second_client(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
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
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Инициализируем драйвер')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.testcase('Клик на лого Самокат')
    @allure.description('Проверяем переход на главную страницу сервера по клику на лого Самокат')
    @allure.title('Клик на лого Самокат')
    def test_click_scooter_logo(self):

        home_page_objects = HomePage(self.driver)
        home_page_objects.click_in_logo_scooter()
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/img')))
        assert self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/img')

    @allure.title('Закрываем драйвер')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Инициализируем драйвер')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.testcase('Нажимаем на логотип Яндекса')
    @allure.description('Проверяем переход на главную страницу сайта Яндекс по клику на логотип Яндекса')
    @allure.title('Нажимаем на логотип Яндекса')
    def test_click_yandex_logo(self):
        home_page = HomePage(self.driver)
        home_page.open_page_scooter()

        handles_before = self.driver.window_handles
        home_page.click_yandex_link()
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(len(handles_before) + 1))

        handles_current = self.driver.window_handles
        new_window = None
        for window in handles_current:
            if window not in handles_before:
                new_window = window
                break

        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'))

        assert self.driver.title == 'Дзен'

    @allure.title('Закрываем драйвер')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
