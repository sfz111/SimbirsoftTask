import random

from faker import Faker

from utils.constants import AUTO_PREFIX

faker = Faker(locale="ru")


def entity_data() -> dict:
    return {
        "addition": {
            "additional_info": faker.sentence(),
            "additional_number": random.randint(0, 1000)
        },
        "important_numbers": [random.randint(0, 100) for _ in range(random.randint(2, 6))],
        "title": f"{AUTO_PREFIX}{random.randint(0, 100000)}",
        "verified": random.choice([True, False])
    }
