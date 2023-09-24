import re
from pydantic import BaseModel, Field, validator, EmailStr
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

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class TaskRead(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    title: str
    description: Optional[str] = None
    status_task: bool = False
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
    status_task: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True
        populate_by_name = True
        json_encoders = {
            ObjectId: str
        }


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status_task: Optional[bool] = None
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }


class UserRead(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    email: str
    nome: Optional[str]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }

class UserWrite(BaseModel):
    email: EmailStr
    password: str
    nome: str

    # Validando campo Username
    @validator('nome')
    def validate_username(cls, value):
        if not re.match("[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ']", 'value'):  
            raise ValueError('Nome com formato inválido')
        return value
    
    # # Validando campo Username
    # @validator('email')
    # def validate_email(cls, value):
    #     if not re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', 'value'):
    #         raise ValueError('Email com formato inválido')
    #    return value
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }


class UserUpdate(BaseModel):
    email: str
    password: str
    nome: Optional[str]

    # Validando campo Username
    @validator('nome')
    def validatee_username(cls, value):
        if not re.match("^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ-']+$", 'value'):  
            raise ValueError('Username com formato inválido')
        return value
    
    # Validando campo Username
    @validator('email')
    def validate_email(cls, value):
        if not re.match('^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$', 'value'):
            raise ValueError('Username com formato inválido')
        return value
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }


class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UserAccess(BaseModel):
    email: str
    access_token: str
    exp: datetime
    

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
   