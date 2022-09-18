from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class PersonalData:

    name = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/input']
    surname = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/input']
    address = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/input']
    station = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div/input']
    station_names_first = [By.XPATH, '//li[@class="select-search__row"][1]']
    station_names_second = [By.XPATH, '//li[@class="select-search__row"][2]']
    phone = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/input']
    next_button = [By.XPATH, '//div[@id="root"]//button[text()="Далее"]']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем сайт')
    def open_site(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

    @allure.step('Вводим имя')
    def fill_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    @allure.step('Вводим фамилию')
    def fill_surname(self, surname):
        self.driver.find_element(*self.surname).send_keys(surname)

    @allure.step('Вводим адрес')
    def fill_address(self, address):
        self.driver.find_element(*self.address).send_keys(address)

    @allure.step('Нажимаем на поле метро')
    def click_field_station(self):
        self.driver.find_element(*self.station).click()

    @allure.step('Указываем станцию метро для первого заказа')
    def station_selection_first(self):
        self.driver.find_element(*self.station_names_first).click()

    @allure.step('Указываем станцию метро для второго заказа')
    def station_selection_second(self):
        self.driver.find_element(*self.station_names_second).click()

    @allure.step('Вводим телефон')
    def fill_phone(self, phone):
        self.driver.find_element(*self.phone).send_keys(phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_next(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Создаем шаг для первого заказа')
    def first_order(self, name, surname, address, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.click_field_station()
        self.station_selection_first()
        self.fill_phone(phone)
        self.click_next()

    @allure.step('Создаем шаг для второго заказа')
    def second_order(self, name, surname, address, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.click_field_station()
        self.station_selection_second()
        self.fill_phone(phone)
        self.click_next()


class RentScooter():

    header = [By.XPATH, '//*[@id="root"]/div/div[2]/div[1]']
    data_input = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]"]
    day_for_first_scooter = [By.XPATH,"/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[6]"]
    day_for_second_scooter = [By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[6]']
    period_dropdown = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]']
    period_dropdown_item_first_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[4]']
    period_dropdown_item_second_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[6]']
    colour_box_first_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/label[1]']
    colour_box_second_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/label[2]']
    comment = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/input']
    order_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем заголовок формы ввода параметров аренды')
    def find_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header))

    @allure.step('Нажимаем на поле дата')
    def click_field_date(self):
        self.driver.find_element(*self.data_input).click()

    @allure.step('Выбираем дату для первого заказа')
    def click_day_first_scooter(self):
        self.driver.find_element(*self.day_for_first_scooter).click()

    @allure.step('Выбираем дату для второго заказа')
    def click_day_second_scooter(self):
        self.driver.find_element(*self.day_for_second_scooter).click()

    @allure.step('Нажимаем на поле периода аренды')
    def click_field_period_dropdown(self):
        self.driver.find_element(*self.period_dropdown).click()

    @allure.step('Выбираем период аренды для первого заказа')
    def choose_period_dropdown_first_scooter(self):
        self.driver.find_element(*self.period_dropdown_item_first_scooter).click()

    @allure.step('Выбираем период аренды для второго заказа')
    def choose_period_dropdown_second_scooter(self):
        self.driver.find_element(*self.period_dropdown_item_second_scooter).click()

    @allure.step('Выбираем цвет для первого заказа')
    def choose_colour_first_scooter(self):
        self.driver.find_element(*self.colour_box_first_scooter).click()

    @allure.step('Выбираем цвет для второго заказа')
    def choose_colour_second_scooter(self):
        self.driver.find_element(*self.colour_box_second_scooter).click()

    @allure.step('Пишем комментарий курьеру')
    def comment_to_the_courier(self, comment):
        self.driver.find_element(*self.comment).send_keys(comment)

    @allure.step('Нажимаем на кнопку заказа')
    def click_button_order(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Создаем шаг аренды для первого заказа')
    def first_scooter(self, comment):
        self.find_header()
        self.click_field_date()
        self.click_day_first_scooter()
        self.click_field_period_dropdown()
        self.choose_period_dropdown_first_scooter()
        self.choose_colour_first_scooter()
        self.comment_to_the_courier(comment)
        self.click_button_order()

    @allure.step('Создаем шаг аренды для второго заказа')
    def second_scooter(self, comment):
        self.find_header()
        self.click_field_date()
        self.click_day_second_scooter()
        self.click_field_period_dropdown()
        self.choose_period_dropdown_second_scooter()
        self.choose_colour_second_scooter()
        self.comment_to_the_courier(comment)
        self.click_button_order()


class OrderConfirmationWindow():

    header = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[1]']
    consent_button = [By.XPATH, '//button[text()="Да"]']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем заголовок окна подтверждения заказа')
    def find_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header))

    @allure.step('Нажимаем на кнопку "Да"')
    def click_consent_button(self):
        self.driver.find_element(*self.consent_button).click()

    @allure.step('Создаем шаг подтверждения первого заказа ')
    def order_confirmation_first_client(self):
        self.find_header()
        self.click_consent_button()

    @allure.step('Создаем шаг подтверждения второго заказа ')
    def order_confirmation_second_client(self):
        self.find_header()
        self.click_consent_button()


class WindowOfCompletedOrder():

    header = [By.XPATH, '//div[text()="Заказ оформлен"]']
    check_status_button = [By.XPATH, '//button[text()="Посмотреть статус"]']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем заголовок модального окна номера заказа')
    def find_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header))

    @allure.step('Кликаем кнопку Посмотреть статус')
    def click_check_status_button(self):
        self.driver.find_element(*self.check_status_button).click()

    @allure.step('Создание шага для просмотра статуса первого заказа')
    def completed_order_first_client(self):
        self.find_header()
        self.click_check_status_button()

    @allure.step('Создание шага для просмотра статуса первого заказа')
    def completed_order_second_client(self):
        self.find_header()
        self.click_check_status_button()






