import allure
import pytest
from allure import step

from utils.constants import FIRST_NAME
from utils.helpers import evalute_name_to_delete


@allure.suite("Менеджер банка")
@allure.sub_suite("Полномочия менеджера")
@pytest.mark.usefixtures("open_manager_page")
class TestCustomers:

    @allure.title("Создание клиента")
    def test_add_customer(self, add_customer_page):
        with step("Добавление клиента"):
            add_customer_page.add_customer()

        with step("Проверка, что появилось сообщение об успешном создании клиента"):
            text = add_customer_page.switch_to_alert_and_get_text().split(" :")[0]
            assert "Customer added successfully with customer id" == text, f"Ожидалось сообщение об успешном создании клиента, но получено: '{text}'"

    @allure.title("Сортировка клиентов по имени")
    def test_sort_customers(self, manager_page, customers_page):
        with step("Переход на страницу клиентов"):
            manager_page.show_customers()

        with step(f"Сортировка клиентов по столбцу '{FIRST_NAME}'"):
            actual_list = customers_page.sort_customers_by_first_name()
        with step("Проверка, что клиенты отсортированы по убыванию"):
            assert sorted(actual_list, reverse=True) == actual_list, "Клиенты не отсортированы по убыванию"

        with step(f"Повторная сортировка клиентов по столбцу '{FIRST_NAME}'"):
            actual_list = customers_page.sort_customers_by_first_name()
        with step("Проверка, что клиенты отсортированы по возрастанию"):
            assert sorted(actual_list) == actual_list, "Клиенты не отсортированы по возрастанию"

    @allure.title("Удаление клиента")
    def test_delete_customer(self, manager_page, customers_page):
        with step("Переход на страницу клиентов"):
            manager_page.show_customers()

        name_to_delete = evalute_name_to_delete(names=customers_page.get_names())
        with step(f"Удаление клиента с именем '{name_to_delete}'"):
            customers_page.delete_customer(name_to_delete)

        with step(f"Проверка, что клиент '{name_to_delete}' не отображается в таблице"):
            customers_page.check_deleted_customer_is_invisible(name_to_delete)
