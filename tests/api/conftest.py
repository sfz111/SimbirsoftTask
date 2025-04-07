from http import HTTPStatus

import pytest
from allure import step

from config import API_URL
from libraries.api.asserts.common_asserts import check_status_code
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
            response = entity_api.delete_entity(id_=request.node.entity_id)
            check_status_code(response, expected_status=HTTPStatus.NO_CONTENT, msg='Не удалось удалить сущность')


@pytest.fixture(scope="function")
def created_entity(entity_api):
    with step("Создание сущности"):
        data = entity_data()
        response = entity_api.create_entity(json=data)
        check_status_code(response, expected_status=HTTPStatus.OK, msg='Не удалось создать сущность')
        entity_id = response.json()

    yield entity_id, data


@pytest.fixture(scope="function")
def create_and_delete_entity(entity_api, created_entity):
    entity_id, data = created_entity
    yield entity_id, data

    with step("Удаление сущности после теста"):
        response = entity_api.delete_entity(id_=entity_id)
        check_status_code(response, expected_status=HTTPStatus.NO_CONTENT, msg='Не удалось удалить сущность')
