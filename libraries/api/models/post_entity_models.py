from pydantic import BaseModel, RootModel


class Addition(BaseModel):
    additional_info: str
    additional_number: int


class EntityPostRequest(BaseModel):
    """Модель запроса создания сущности"""
    addition: Addition
    important_numbers: list[int]
    title: str
    verified: bool


StringResponse = RootModel[int]
