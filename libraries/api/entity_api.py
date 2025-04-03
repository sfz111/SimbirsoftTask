from requests import Response

from libraries.api.base_api import BaseApi
from libraries.api.models.get_entities_models import EntitiesGetResponse
from libraries.api.models.get_entity_models import EntityGetResponse
from libraries.api.models.patch_entity_models import EntityPatchRequest
from libraries.api.models.post_entity_models import EntityPostRequest, StringResponse


class EntityApi(BaseApi):
    POST_URL = "/api/create"
    DELETE_URL = "/api/delete"
    GET_URL = "/api/get"
    GET_ALL = "/api/getAll"
    PATCH_URL = "/api/patch"

    def create_entity(self, json: dict, **kwargs) -> Response:
        """Создание сущности"""
        response = self.post(request_url=self.POST_URL, json=EntityPostRequest.model_validate(json).model_dump(),
                             **kwargs)
        return self.validate_response(response, response_schema=StringResponse)

    def delete_entity(self, id_: str, **kwargs) -> Response:
        """Удаление сущности"""

        return self.delete(request_url=f"{self.DELETE_URL}/{id_}", **kwargs)

    def get_entity(self, id_: str, **kwargs) -> Response:
        """Получение сущности по id"""

        response = self.get(request_url=f"{self.GET_URL}/{id_}", **kwargs)
        return self.validate_response(response, response_schema=EntityGetResponse)

    def get_entities(self, title: str = "", verified: bool = None, page: int = None, per_page: int = None,
                     **kwargs) -> Response:
        """Получение сущностей"""

        params = kwargs.get("params", {})
        if title is not None:
            params["title"] = title
        if verified is not None:
            params["verified"] = verified
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["perPage"] = per_page

        response = self.get(request_url=self.GET_ALL, params=params, **kwargs)
        return self.validate_response(response, response_schema=EntitiesGetResponse)

    def update_entity(self, id_: str, json: dict, **kwargs) -> Response:
        """Обновление сущности"""

        return self.patch(request_url=f"{self.PATCH_URL}/{id_}",
                          json=EntityPatchRequest.model_validate(json).model_dump(), **kwargs)
