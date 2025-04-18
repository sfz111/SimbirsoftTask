from http import HTTPStatus

import allure
from allure import step
from deepdiff import DeepDiff

from libraries.api.asserts.common_asserts import check_status_code
from tests.api.conftest import entity_api
from tests.api.data_generation import entity_data
from utils.helpers import format_diff


@allure.suite("API тесты")
@allure.sub_suite("Entity api")
class TestEntity:

    @allure.title("Успешное создание сущности с обязательными полями")
    def test_create_entity(self, entity_api, request, entity_teardown):
        with step("Создание сущности"):
            created_entity_data = entity_data()
            response = entity_api.create_entity(json=created_entity_data)

        with step("Проверка, что сущность создана"):
            check_status_code(response, expected_status=HTTPStatus.OK, msg='Не удалось создать сущность')
            entity_id = response.json()
            request.node.entity_id = entity_id

        with step(f"Получение созданной сущности по id {entity_id}"):
            get_response = entity_api.get_entity(id_=entity_id)
            check_status_code(response, expected_status=HTTPStatus.OK, msg='Не удалось получить созданную сущность')
            assert get_response.json()['id'] == entity_id, 'id из ответа не совпадает с id созданной сущности'

    @allure.title("Успешное обновление сущности")
    def test_update_entity(self, entity_api, create_and_delete_entity):
        entity_id, _ = create_and_delete_entity
        with step("Обновление сущности"):
            new_data = entity_data()
            response = entity_api.update_entity(id_=entity_id, json=new_data)

        with step("Проверка, что сущность обновлена"):
            check_status_code(response, expected_status=HTTPStatus.NO_CONTENT, msg='Не удалось обновить сущность')

        with step(f"Получение созданной сущности по id {entity_id}"):
            get_response = entity_api.get_entity(id_=entity_id)
            check_status_code(response, expected_status=HTTPStatus.OK, msg='Не удалось получить сущность')

        with step("Проверка, что значения в ответе содержат обновленные данные"):
            diff = DeepDiff(new_data, get_response.json(), ignore_order=True,
                            exclude_paths=["root['id']", "root['addition']['id']"])
            assert not diff, f"Данные в полях не совпадают:\n{format_diff(diff)}"

    @allure.title("Успешное удаление существующей сущности")
    def test_delete_entity(self, entity_api, created_entity):
        entity_id, _ = created_entity
        with step("Удаление сущности"):
            response = entity_api.delete_entity(id_=entity_id)

        with step("Проверка, что сущность удалена"):
            check_status_code(response, expected_status=HTTPStatus.NO_CONTENT, msg='Не удалось удалить сущность')

    @allure.title("Успешное получение данных существующей сущности")
    def test_get_entity(self, entity_api, create_and_delete_entity):
        entity_id, data = create_and_delete_entity
        with step("Получение сущности по id"):
            response = entity_api.get_entity(id_=entity_id)

        with step("Проверка, что сущность получена"):
            check_status_code(response, expected_status=HTTPStatus.OK, msg='Не удалось получить сущность')
            assert response.json()['id'] == entity_id, 'id из ответа не совпадает с id созданной сущности'

        with step("Проверка, что значения в ответе содержат данные созданной сущности"):
            diff = DeepDiff(data, response.json(), ignore_order=True,
                            exclude_paths=["root['id']", "root['addition']['id']"])
            assert not diff, f"Данные в полях не совпадают:\n{format_diff(diff)}"

    @allure.title("Успешное получение списка существующих сущностей")
    def test_get_entities(self, entity_api, create_and_delete_entity):
        with step("Получение списка всех сущностей"):
            response = entity_api.get_entities()

        with step("Проверка, что возвращается список сущностей"):
            check_status_code(response, expected_status=HTTPStatus.OK, msg='Не удалось получить список сущностей')
            assert len(response.json()) > 0, 'В списке не оказалось сущностей'
