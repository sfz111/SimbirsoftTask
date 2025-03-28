import allure
import pytest
from allure_commons.types import AttachmentType
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from env import MANAGER_URL
from ui.manager.add_customer_page import AddCustomerPage
from ui.manager.customers_page import CustomersPage
from ui.manager.manager_page import ManagerPage


@pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):
    yield

    if report.failed and "driver" in node.funcargs:
        driver = node.funcargs["driver"]
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Скриншот при падении",
                attachment_type=AttachmentType.PNG
            )

        except Exception as e:
            print(f"Не удалось сохранить скриншот: {e}")


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )


@fixture(scope="function")
def driver(request):
    """Инициализация драйвера"""

    options = Options()
    options.page_load_strategy = 'eager'
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    request.cls.driver = driver
    driver.maximize_window()
    driver.get(MANAGER_URL)

    yield driver
    driver.quit()


@fixture(scope="function")
def manager_page(driver):
    yield ManagerPage(driver)


@fixture(scope="function")
def add_customer_page(driver):
    yield AddCustomerPage(driver)


@fixture(scope="function")
def customers_page(driver):
    yield CustomersPage(driver)
