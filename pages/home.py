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

    headers = [By.XPATH, '//*[@id="root"]/div/div/div[5]/div[2]']
    questions = [By.XPATH, '//*[@id="root"]//div[@class="accordion"]//div[@class="accordion__item"]']
    question_button = [By.CLASS_NAME, 'accordion__button']
    answer = [By.CLASS_NAME, 'accordion__panel']
    faq_items = []

    @allure.step('Инициализируем драйвер в объекте FaqQuestions')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем заголовок FAQ')
    def get_header(self):
        return self.driver.find_element(*self.headers)

    @allure.step('Скролл к списку FAQ')
    def scroll_to_header(self):
        header = self.get_header()
        self.driver.execute_script('arguments[0].scrollIntoView();', header)

    @allure.step('Возвращаем вопросы из FAQ')
    def get_questions(self):
        return self.driver.find_elements(*self.questions)

    @allure.step('Получаем пункт FAQ по вопросу')
    def get_faq_by_question(self, question):
        try:
            return self.driver.find_element(By.XPATH,f'//*[@class="accordion__button" and text()='f'"{question}"]/parent::*/parent::*')
        except AttributeError:
            return None

    @allure.step('Находим кнопку в пункте FAQ')
    def get_question_button(self, question):
        return question.find_element(*self.question_button)

    @allure.step('Раскрываем пункт в списке FAQ')
    def click_question_button(self, question):
        self.get_question_button(question).click()

    @allure.step('Получаем ответ')
    def get_answer(self, question):
        answer = question.find_element(*self.answer)
        return answer.find_element(By.XPATH, './/p').text

    @allure.step('Сохраняем данные списка FAQ')
    def get_faq(self):
        questions = self.get_questions()
        for question in questions:
            self.click_question_button(question)
            self.driver.implicitly_wait(1)
            question_text, answer_text = question.text.split('\n')
            self.faq_items.append({'question': question_text, 'answer': answer_text})
        return self.faq_items


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


