from pydantic import BaseModel, field_validator
from typing import Optional

class UbicacionBase(BaseModel):
    id_ubicacion: Optional[int] = None
    nombre: str
    id_facultad: int

    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, value: str):
        if not value or not value.strip():
            raise ValueError('El nombre de la ubicación es obligatorio')
        return value.strip()

    class Config:
        from_attributes = True