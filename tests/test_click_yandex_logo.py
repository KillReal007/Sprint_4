from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from pages.home import HomePage


class TestClickYandexLogo():
    driver = None

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