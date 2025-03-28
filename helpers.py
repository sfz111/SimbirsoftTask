from random import randint

import allure
from allure import step
from faker import Faker

from constants import POST_CODE, FIRST_NAME

faker = Faker()


def evalute_name_to_delete(names: list[str]) -> str:
    """
    Возвращает имя из списка, длина которого ближе всего к средней длине всех имен.
    """
    names_dict = {name: len(name) for name in names}

    avg_len = sum(names_dict.values()) / len(names)

    minimum = 0
    name_to_delete = ''
    for name, name_len in names_dict.items():
        diff = avg_len - name_len
        if diff <= minimum:
            minimum = diff
            name_to_delete = name

    return name_to_delete


def generate_post_code() -> str:
    post_code = ''.join([str(randint(0, 9)) for _ in range(10)])
    return post_code


def generate_first_name(post_code: str) -> str:
    with step(f"Генерируем '{FIRST_NAME}' на основе значения из поля '{POST_CODE}'"):
        pairs = []
        for i in range(0, len(post_code), 2):
            pairs.append(int(f'{post_code[i]}{post_code[i + 1]}'))

        first_name = []
        for num in pairs:
            if num > 25:
                num = num % 26
            letter = chr(ord('a') + num)
            first_name.append(letter)

        return ''.join(first_name)


def generate_last_name() -> str:
    return faker.last_name()
