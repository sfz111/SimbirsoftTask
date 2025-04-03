import allure
from allure import step
from deepdiff import DeepDiff

from tests.api.conftest import entity_api
from tests.api.data_generation import entity_data
from utils.helpers import format_diff


@allure.suite("API тесты")
@allure.sub_suite("Entity api")
class TestEntity:

    @allure.title("Создание сущности")
    def test_create_entity(self, entity_api, request, entity_teardown):
        with step("Создание сущности"):
            response = entity_api.create_entity(json=entity_data())

        with step("Проверка, что сущность создана"):
            assert response.status_code == 200, 'Не удалось создать сущность'
            entity_id = response.json()
            request.node.entity_id = entity_id

        with step(f"Получение созданной сущности по id {entity_id}"):
            get_response = entity_api.get_entity(id_=entity_id)
            assert get_response.status_code == 200, 'Не удалось получить созданную сущность'
            assert get_response.json()['id'] == entity_id

    @allure.title("Обновление сущности")
    def test_update_entity(self, entity_api, create_and_delete_entity):
        with step("Обновление сущности"):
            new_data = entity_data()
            response = entity_api.update_entity(id_=create_and_delete_entity, json=new_data)

        with step("Проверка, что сущность обновлена"):
            assert response.status_code == 204, 'Не удалось обновить сущность'

        with step(f"Получение созданной сущности по id {create_and_delete_entity}"):
            get_response = entity_api.get_entity(id_=create_and_delete_entity)
            assert get_response.status_code == 200, 'Не удалось получить сущность'

            diff = DeepDiff(new_data, get_response.json(), ignore_order=True,
                            exclude_paths=["root['id']", "root['addition']['id']"])

            assert not diff, f"Данные в полях не совпадают:\n{format_diff(diff)}"

    @allure.title("Удаление сущности")
    def test_delete_entity(self, entity_api, created_entity):
        with step("Удаление сущности"):
            response = entity_api.delete_entity(id_=created_entity)

        with step("Проверка, что сущность удалена"):
            assert response.status_code == 204, 'Не удалось удалить сущность'

    @allure.title("Получение сущности по id")
    def test_get_entity(self, entity_api, create_and_delete_entity):
        with step("Получение сущности по id"):
            response = entity_api.get_entity(id_=create_and_delete_entity)

        with step("Проверка, что сущность получена"):
            assert response.status_code == 200, 'Не удалось получить сущность'
            assert response.json()['id'] == create_and_delete_entity

    @allure.title("Получение списка сущностей")
    def test_get_entities(self, entity_api, create_and_delete_entity):
        with step("Получение списка всех сущностей"):
            response = entity_api.get_entities()

        with step("Проверка, что возвращается список сущностей"):
            assert response.status_code == 200, 'Не удалось получить список сущностей'
            assert len(response.json()) > 0, 'В списке не оказалось сущностей'
