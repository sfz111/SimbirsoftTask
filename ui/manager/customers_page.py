from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.base_page import BasePage


class CustomersPage(BasePage):
    FIRST_NAME_COLUMN = (By.XPATH, "//a[contains(@ng-click,\"sortType = 'fName'\")]")
    FIRST_NAME_CUSTOMER = (By.XPATH, "//tr[contains(@ng-repeat,'searchCustomer')]/td[1]")
    DELETE_BUTTON_BY_NAME = staticmethod(
        lambda text: (By.XPATH, f'//td[text()="{text}"]/..//button[@ng-click="deleteCust(cust)"]'))
    TABLE_BODY = (By.TAG_NAME, 'tbody')
    TABLE_ROW = staticmethod(lambda text: (By.XPATH, f'//td[text()="{text}"]/parent::tr'))

    def sort_customers_by_first_name(self) -> list[str]:
        self.click(self.FIRST_NAME_COLUMN)
        return self.get_names()

    def get_names(self) -> list[str]:
        names = []
        self.wait.until(EC.visibility_of_element_located(self.TABLE_BODY),
                        "Тело таблицы клиентов не отображается на странице")
        for element in self.elements(self.FIRST_NAME_CUSTOMER):
            names.append(element.text)

        return names

    def delete_customer(self, name: str):
        self.click(self.DELETE_BUTTON_BY_NAME(name))

    def check_deleted_customer_is_invisible(self, name: str):
        self.wait.until(EC.invisibility_of_element_located(self.TABLE_ROW(name)),
                        f"Клиент с именем '{name}' отображается на странице")
