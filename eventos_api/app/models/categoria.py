from pydantic import BaseModel, field_validator
from typing import Optional

class CategoriaBase(BaseModel):
    id_categoria: Optional[int] = None
    nombre: str

    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, value: str):
        if not value or not value.strip():
            raise ValueError('El nombre de la categoría es obligatorio')
        return value.strip()

    class Config:
        from_attributes = True