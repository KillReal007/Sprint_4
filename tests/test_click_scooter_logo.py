from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure
from pages.home import HomePage


class TestClickScooterLogo():
    driver = None

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