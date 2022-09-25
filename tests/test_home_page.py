import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pages.home import FaqQuestions
from pages.base import BasePage
from pages.home import HomePage


class TestHomePage:

    @allure.title('Инициализируем драйвер')
    def setup(self):
        self.driver = webdriver.Firefox()

    @allure.title('Проверка вопроса FAQ')
    @allure.description('Проверяем первый вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_first_question(self):
        click = FaqQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_first_question()
        assert self.driver.find_element(By.XPATH, '//*[@id="accordion__panel-0"]/p')

    @allure.title('Проверка вопроса FAQ')
    @allure.description('Проверяем второй вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_second_question(self):
        click = FaqQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_second_question()
        assert self.driver.find_element(By.XPATH, '//*[@id="accordion__panel-1"]/p')

    @allure.title('Проверка вопроса FAQ')
    @allure.description('Проверяем третий вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_third_question(self):
        click = FaqQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_third_question()
        assert self.driver.find_element(By.XPATH, '//*[@id="accordion__panel-2"]/p')

    @allure.title('Проверка вопроса FAQ')
    @allure.description('Проверяем четвертый вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_fourth_question(self):
        click = FaqQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_fourth_question()
        assert self.driver.find_element(By.XPATH, '//*[@id="accordion__panel-3"]/p')

    @allure.title('Проверка вопроса FAQ')
    @allure.description('Проверяем пятый вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_fifth_question(self):
        click = FaqQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_fifth_question()
        assert self.driver.find_element(By.XPATH, '//*[@id="accordion__panel-4"]/p')

    @allure.title('Проверка вопроса FAQ')
    @allure.description('Проверяем шестой вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_sixth_question(self):
        click = FaqQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_sixth_question()
        assert self.driver.find_element(By.XPATH, '//*[@id="accordion__panel-5"]/p')

    @allure.title('Проверка вопроса FAQ')
    @allure.description('Проверяем седьмой вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_seventh_question(self):
        click = FaqQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_seventh_question()
        assert self.driver.find_element(By.XPATH, '//*[@id="accordion__panel-6"]/p')

    @allure.title('Проверка вопроса FAQ')
    @allure.description('Проверяем восьмой вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_eighth_question(self):
        click = FaqQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_eighth_question()
        assert self.driver.find_element(By.XPATH, '//*[@id="accordion__panel-7"]/p')

    @allure.testcase('Нажимаем на логотип Самокат')
    @allure.description('Проверяем переход на главную страницу сервера по клику на лого Самокат')
    @allure.title('Нажимаем на логотип Самокат')
    def test_click_scooter_logo(self):
        home_page_objects = HomePage(self.driver)
        home_page_objects.click_in_logo_scooter()
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/img')))
        assert self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/img')

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
    def teardown(self):
        self.driver.quit()