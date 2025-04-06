import random

from pydantic import BaseModel, RootModel, Field

from utils.constants import AUTO_PREFIX
from utils.data_generation import faker


class Addition(BaseModel):
    additional_info: str = Field(default_factory=lambda: faker.sentence())
    additional_number: int = Field(default_factory=lambda: faker.random_int(min=0, max=1000))


class EntityPostRequest(BaseModel):
    """Модель запроса создания сущности"""

    addition: Addition = Field(default_factory=Addition)
    important_numbers: list[int] = Field(
        default_factory=lambda: [faker.random_int(min=0, max=100) for _ in range(faker.random_int(min=2, max=5))]
    )
    title: str = Field(
        default_factory=lambda: f"{AUTO_PREFIX}{faker.random_int(min=0, max=100000)}"
    )
    verified: bool = Field(default_factory=lambda: random.choice([True, False]))


StringResponse = RootModel[int]
