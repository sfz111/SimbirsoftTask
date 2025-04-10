from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str
    additional_number: int
    id: int


class ModelItem(BaseModel):
    addition: Addition
    id: int
    important_numbers: list[int]
    title: str
    verified: bool


class EntitiesGetResponse(BaseModel):
    """Модель ответа получения сущностей"""
    entity: list[ModelItem]
