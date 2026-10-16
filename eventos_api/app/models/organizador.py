from pydantic import BaseModel, field_validator
from typing import Optional

class OrganizadorBase(BaseModel):
    id_organizador: Optional[int] = None
    id_usuario: int

    @field_validator('id_usuario')
    @classmethod
    def validar_usuario(cls, value: int):
        if value <= 0:
            raise ValueError('El ID de usuario debe ser válido')
        return value

    class Config:
        from_attributes = True