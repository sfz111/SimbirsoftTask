from requests import Response


def check_status_code(response: Response, expected_status: int, msg: str):
    """ Метод проверки статус кода """
    assert response.status_code == expected_status, msg
