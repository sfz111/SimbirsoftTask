from allure import step
from requests import session, Response

from libraries.allure_helpers import allure_attach


class BaseApi:

    def __init__(self, api_url: str):
        self.api_url = api_url
        self.session = session()

    @allure_attach
    def post(self, request_url: str, **kwargs):
        return self._send_request(method="POST", request_url=request_url, **kwargs)

    @allure_attach
    def get(self, request_url: str, **kwargs):
        return self._send_request(method="GET", request_url=request_url, **kwargs)

    @allure_attach
    def patch(self, request_url: str, **kwargs):
        return self._send_request(method="PATCH", request_url=request_url, **kwargs)

    @allure_attach
    def delete(self, request_url: str, **kwargs):
        return self._send_request(method="DELETE", request_url=request_url, **kwargs)

    def _send_request(self, method: str, request_url: str, **kwargs):
        full_url = f"{self.api_url}{request_url}"

        with step(f"Отправка запроса {method} {full_url}"):
            response = self.session.request(method=method, url=full_url, **kwargs)

        return response

    @staticmethod
    def validate_response(response: Response, response_schema, empty_body: bool = False) -> Response:
        if not empty_body:
            response_schema.model_validate(response.json())
        return response
