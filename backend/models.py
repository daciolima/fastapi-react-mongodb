from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional
from bson import ObjectId
from datetime import datetime


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    # Validadores
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('ObjectId Inválido')
        return str(v)


class TaskRead(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    title: str
    description: Optional[str] = None
    status: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True
        populate_by_name = True
        json_encoders = {
            ObjectId: str
        }


class TaskWrite(BaseModel):
    title: str
    description: Optional[str] = None
    status: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True
        populate_by_name = True
        json_encoders = {
            ObjectId: str
        }


class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }