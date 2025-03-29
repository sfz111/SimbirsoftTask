from typing import Union

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=5)

    def element(self, locator: tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)

    def elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def input_field(self, locator: tuple[str, str], text: str):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def click(self, locator: Union[WebElement, tuple[str, str]]):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def switch_to_alert_and_get_text(self) -> str:
        alert = self.wait.until(EC.alert_is_present(), "Алерт не появился")
        text = self.driver.switch_to.alert.text
        alert.accept()
        return text

    def should_be_visible(self, locator: tuple[str, str], msg: str = None):
        self.wait.until(EC.visibility_of_element_located(locator), message=msg)

    def should_be_invisible(self, locator: WebElement | tuple[str, str], msg: str = None):
        self.wait.until(EC.invisibility_of_element_located(locator), message=msg)