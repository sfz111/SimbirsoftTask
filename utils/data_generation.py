from random import randint

from allure import step
from faker import Faker

from utils.constants import POST_CODE, FIRST_NAME

faker = Faker()


def generate_post_code() -> str:
    """ Генерация строки из 10 цифр для поля post code """
    post_code = ''.join([str(randint(0, 9)) for _ in range(10)])
    return post_code


def generate_first_name(post_code: str) -> str:
    """
    Генерация имени на основе значения из поля post code по алгоритму:
    Разбиваем Post Code на 5 двузначных чисел (например, 12 34 56 78 90).
    Преобразовываем каждое число в букву английского алфавита по правилу: 0 → a, 1 → b, ..., 25 → z
    """
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
    """Генерация строки для поля Last Name"""
    return faker.last_name()
