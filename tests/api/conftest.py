import pytest
from allure import step

from config import API_URL
from libraries.api.entity_api import EntityApi
from tests.api.data_generation import entity_data


@pytest.fixture(scope="function")
def entity_api():
    yield EntityApi(api_url=API_URL)


@pytest.fixture(scope="function")
def entity_teardown(entity_api, request):
    yield
    if hasattr(request.node, 'entity_id'):
        with step("Удаление сущности, созданной в тесте"):
            entity_api.delete_entity(id_=request.node.entity_id)


@pytest.fixture(scope="function")
def created_entity(entity_api):
    with step("Создание сущности"):
        response = entity_api.create_entity(json=entity_data())
        assert response.status_code == 200
        entity_id = response.json()

    yield entity_id


@pytest.fixture(scope="function")
def create_and_delete_entity(entity_api, created_entity):
    yield created_entity

    with step("Удаление сущности после теста"):
        response = entity_api.delete_entity(id_=created_entity)
        assert response.status_code == 204
