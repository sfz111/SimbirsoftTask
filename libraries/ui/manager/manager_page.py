from selenium.webdriver.common.by import By

from libraries.ui.base_page import BasePage


class ManagerPage(BasePage):
    ADD_CUSTOMER_BTN = (By.CSS_SELECTOR, '[ng-click="addCust()"]')
    OPEN_ACCOUNT_BTN = (By.CSS_SELECTOR, '[ng-click="openAccount()"]')
    SHOW_CUSTOMERS_BTN = (By.CSS_SELECTOR, '[ng-click="showCust()"]')

    def open_account(self):
        self.click(self.OPEN_ACCOUNT_BTN)

    def show_customers(self):
        self.click(self.SHOW_CUSTOMERS_BTN)
