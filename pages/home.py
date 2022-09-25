from selenium.webdriver.common.by import By
import allure
from pages.base import BasePage

class ButtonOrder:

    button = [By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/button[1]']

    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self):
        self.driver.find_element(*self.button).click()

class Cookies:

    cookie_button = [By.ID, 'rcc-confirm-button']
    cookies = None

    @allure.step('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим кнопку для установки cookies и кликаем по ней')
    def click_consent_button(self):
        self.driver.find_element(*self.cookie_button).click()

    @allure.step('Сохраняем куки')
    def get_cookies(self):
        self.click_consent_button()
        return self.driver.get_cookies()


class FaqQuestions:
    header = [By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]']
    first_question = [By.CSS_SELECTOR, '#accordion__heading-0']
    second_question = [By.CSS_SELECTOR, '#accordion__heading-1']
    third_question = [By.CSS_SELECTOR, '#accordion__heading-2']
    fourth_question = [By.CSS_SELECTOR, '#accordion__heading-3']
    fifth_question = [By.CSS_SELECTOR, '#accordion__heading-4']
    sixth_question = [By.CSS_SELECTOR, '#accordion__heading-5']
    seventh_question = [By.CSS_SELECTOR, '#accordion__heading-6']
    eighth_question = [By.CSS_SELECTOR, '#accordion__heading-7']

    @allure.step('Инициализируем драйвер в объекте FaqQuestions')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем заголовок FAQ')
    def get_header(self):
        return self.driver.find_element(*self.header)

    @allure.step('Скролл к списку FAQ')
    def scroll_to_header(self):
        header = self.get_header()
        self.driver.execute_script('arguments[0].scrollIntoView();', header)

    @allure.step('Нажимаем на первый вопрос')
    def click_first_question(self):
        self.driver.find_element(*self.first_question).click()

    @allure.step('Нажимаем на второй вопрос')
    def click_second_question(self):
        self.driver.find_element(*self.second_question).click()

    @allure.step('Нажимаем на третий вопрос')
    def click_third_question(self):
        self.driver.find_element(*self.third_question).click()

    @allure.step('Нажимаем на четвертый вопрос')
    def click_fourth_question(self):
        self.driver.find_element(*self.fourth_question).click()

    @allure.step('Нажимаем на пятый вопрос')
    def click_fifth_question(self):
        self.driver.find_element(*self.fifth_question).click()

    @allure.step('Нажимаем на шестой вопрос')
    def click_sixth_question(self):
        self.driver.find_element(*self.sixth_question).click()

    @allure.step('Нажимаем на седьмой вопрос')
    def click_seventh_question(self):
        self.driver.find_element(*self.seventh_question).click()

    @allure.step('Нажимаем на восьмой вопрос')
    def click_eighth_question(self):
        self.driver.find_element(*self.eighth_question).click()


class HomePage:
    button_order = [By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/button[1]']
    scooter_link = [By.XPATH, '/html/body/div/div/div[1]/div[1]/a[2]/img']
    yandex_link = [By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/a[1]/img']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    @allure.step('Открываем главную страницу заказа самоката')
    def open_page_scooter(self):
        base = BasePage(self.driver)
        base.open_home_page()

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()

    @allure.step('Нажимаем по логотипу Самокат')
    def click_logo_scooter(self):
        self.driver.find_element(*self.scooter_link).click()

    @allure.step('Нажимаем по логотипу Яндекса')
    def click_yandex_link(self):
        self.driver.find_element(*self.yandex_link).click()

    @allure.step('Создаем шаг для нажатия на логотип самоката')
    def click_in_logo_scooter(self):
        self.open_page_scooter()
        self.click_button_order()
        self.click_logo_scooter()


