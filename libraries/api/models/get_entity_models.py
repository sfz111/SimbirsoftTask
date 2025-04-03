from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str
    additional_number: int
    id: int


class EntityGetResponse(BaseModel):
    """Модель ответа получения сущности"""
    addition: Addition
    id: int
    important_numbers: list[int]
    title: str
    verified: bool
