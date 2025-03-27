from random import randint

import allure
from faker import Faker

from constants import POST_CODE, FIRST_NAME

faker = Faker()


@allure.step("Вычисляем имя для удаления")
def evalute_name_to_delete(names: list[str]) -> str:
    """
    Возвращает имя из списка, длина которого ближе всего к средней длине всех имен.
    """
    names_dict = {name: len(name) for name in names}

    avg_len = sum(names_dict.values()) / len(names)

    minimum = 0
    min_key = ''
    for key, value in names_dict.items():
        diff = avg_len - value
        if diff <= minimum:
            minimum = diff
            min_key = key

    return min_key


def generate_post_code() -> str:
    return ''.join([str(randint(0, 9)) for _ in range(10)])


@allure.step(f"Генерируем '{FIRST_NAME}' на основе значения из поля '{POST_CODE}'")
def generate_first_name(post_code: str) -> str:
    first_name = []
    for i in range(0, len(post_code), 2):
        first_name.append(int(f'{post_code[i]}{post_code[i + 1]}'))
    result = []
    for num in first_name:
        if num > 25:
            num = num % 26
        letter = chr(ord('a') + num)
        result.append(letter)
    return ''.join(result)


def generate_last_name() -> str:
    return faker.last_name()
