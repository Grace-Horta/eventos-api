from pydantic import BaseModel, field_validator
from typing import Optional

class ProgramaBase(BaseModel):
    id_programa: Optional[int] = None
    nombre: str
    id_facultad: int

    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, value: str):
        if not value or not value.strip():
            raise ValueError('El nombre del programa es obligatorio')
        return value.strip()

    @field_validator('id_facultad')
    @classmethod
    def validar_facultad(cls, value: int):
        if value <= 0:
            raise ValueError('El ID de facultad debe ser válido')
        return value

    class Config:
        from_attributes = True