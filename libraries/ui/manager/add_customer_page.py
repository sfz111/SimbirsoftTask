from allure import step
from selenium.webdriver.common.by import By

from utils.constants import FIRST_NAME, POST_CODE, ADD_CUSTOMER, LAST_NAME
from libraries.ui.manager.manager_page import ManagerPage
from utils.data_generation import generate_first_name, generate_last_name, generate_post_code


class AddCustomerPage(ManagerPage):
    ADD_CUSTOMER_FORM = (By.CSS_SELECTOR, '[ng-submit="addCustomer()"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[ng-model="fName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[ng-model="lName"]')
    POST_CODE_INPUT = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    ADD_CUSTOMER_SUBMIT_BTN = (By.CSS_SELECTOR, '[type="submit"]')

    def add_customer(self):
        with step(f"Клик на кнопку '{ADD_CUSTOMER}'"):
            self.click(self.ADD_CUSTOMER_BTN)
        with step("Проверка, что открыта форма добавления клиента"):
            self.should_be_visible(self.ADD_CUSTOMER_FORM, msg="Форма добавления клиента не отображается на странице")

        with step(f"Заполнение поля '{POST_CODE}'"):
            self.input_field(self.POST_CODE_INPUT, post_code := generate_post_code())
        with step(f"Заполнение поля '{FIRST_NAME}'"):
            self.input_field(self.FIRST_NAME_INPUT, text=generate_first_name(post_code))
        with step(f"Заполнение поля '{LAST_NAME}'"):
            self.input_field(self.LAST_NAME_INPUT, text=generate_last_name())

        with step(f"Клик на кнопку '{ADD_CUSTOMER}'"):
            self.click(self.ADD_CUSTOMER_SUBMIT_BTN)
