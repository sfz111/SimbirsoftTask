import pytest
from allure import step

from config import API_URL
from libraries.api.entity_api import EntityApi
from libraries.api.models.post_entity_models import EntityPostRequest


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
        data = EntityPostRequest().model_dump()
        response = entity_api.create_entity(json=data)
        assert response.status_code == 200
        entity_id = response.json()

    yield entity_id, data


@pytest.fixture(scope="function")
def create_and_delete_entity(entity_api, created_entity):
    entity_id, data = created_entity
    yield entity_id, data

    with step("Удаление сущности после теста"):
        response = entity_api.delete_entity(id_=entity_id)
        assert response.status_code == 204
