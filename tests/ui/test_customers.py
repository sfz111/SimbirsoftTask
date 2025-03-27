import allure
from allure import step

from constants import FIRST_NAME
from helpers import evalute_name_to_delete


class TestCustomers:
    @allure.title("Создание клиента")
    def test_add_customer(self, add_customer_page):
        with step("Создаем клиента"):
            add_customer_page.add_customer()

        with step("Проверяем, что появилось сообщение об успешном создании клиента"):
            text = add_customer_page.switch_to_alert_and_get_text()
            assert "Customer added successfully" in text

    @allure.title("Сортировка клиентов по имени")
    def test_sort_customers(self, manager_page, customers_page):
        with step("Открываем страницу клиентов"):
            manager_page.show_customers()

        with step(f"Сортируем клиентов по столбцу '{FIRST_NAME}'"):
            actual_list = customers_page.sort_customers_by_first_name()
        with step("Проверяем что клиенты отсортированы по убыванию"):
            assert sorted(actual_list, reverse=True) == actual_list

        with step(f"Еще раз сортируем клиентов по столбцу '{FIRST_NAME}'"):
            actual_list = customers_page.sort_customers_by_first_name()
        with step("Проверяем что клиенты отсортированы по возрастанию"):
            assert sorted(actual_list) == actual_list

    @allure.title("Удаление клиента")
    def test_delete_customer(self, manager_page, customers_page):
        with step("Открываем страницу клиентов"):
            manager_page.show_customers()

        name_to_delete = evalute_name_to_delete(names=customers_page.get_names())
        with step(f"Удаляем клиента с именем '{name_to_delete}'"):
            customers_page.delete_customer(name_to_delete)

        with step("Проверяем, что удаленный клиент не отображается в таблице"):
            customers_page.check_deleted_customer_is_invisible(name_to_delete)
