import uuid

import requests
import structlog
from allure import step
from requests import session, Response

from libraries.allure_helpers import allure_attach
from utils.logger import configure_logger


class BaseApi:

    def __init__(self, api_url: str):
        self.api_url = api_url
        self.session = session()
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')
        configure_logger()

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

    def _send_request(self, method: str, request_url: str, **kwargs) -> Response:
        full_url = f"{self.api_url}{request_url}"

        log = self.log.bind(event_id=str(uuid.uuid4()))
        request_info = {
            "method": method,
            "url": full_url,
            "params": kwargs.get('params'),
            "headers": kwargs.get('headers'),
            "body": kwargs.get('json') or kwargs.get('data')
        }

        log.info(
            "Request",
            **{k: v for k, v in request_info.items() if v is not None}
        )

        with step(f"Отправка запроса {method} {full_url}"):
            response = self.session.request(method=method, url=full_url, **kwargs)

        response_info = {
            "status": response.status_code,
            "headers": dict(response.headers),
            "body": self._get_json(response),
            "size": len(response.content),
            "time": response.elapsed.total_seconds() if response.elapsed else None
        }

        log.info(
            "Response",
            **{k: v for k, v in response_info.items() if v is not None}
        )

        return response

    @staticmethod
    def validate_response(response: Response, response_schema, empty_body: bool = False) -> Response:
        if not empty_body:
            response_schema.model_validate(response.json())
        return response

    @staticmethod
    def _get_json(response):
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return
