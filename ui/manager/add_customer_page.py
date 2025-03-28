from allure import step
from selenium.webdriver.common.by import By

from constants import FIRST_NAME, POST_CODE, ADD_CUSTOMER, LAST_NAME
from data_generation import generate_first_name, generate_last_name, generate_post_code
from ui.manager.manager_page import ManagerPage


class AddCustomerPage(ManagerPage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[ng-model="fName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[ng-model="lName"]')
    POST_CODE_INPUT = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    ADD_CUSTOMER_SUBMIT_BTN = (By.CSS_SELECTOR, '[type="submit"]')

    def add_customer(self):
        with step(f"Нажимаем на кнопку '{ADD_CUSTOMER}'"):
            self.click(self.ADD_CUSTOMER_BTN)

        with step(f"Заполняем поле '{POST_CODE}'"):
            post_code = generate_post_code()
            self.input_field(self.POST_CODE_INPUT, post_code)
        with step(f"Заполняем поле '{FIRST_NAME}'"):
            self.input_field(self.FIRST_NAME_INPUT, text=generate_first_name(post_code))
        with step(f"Заполняем поле '{LAST_NAME}'"):
            self.input_field(self.LAST_NAME_INPUT, text=generate_last_name())

        with step(f"Нажимаем на кнопку '{ADD_CUSTOMER}'"):
            self.click(self.ADD_CUSTOMER_SUBMIT_BTN)
