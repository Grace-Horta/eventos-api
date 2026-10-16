from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional

class EventoBase(BaseModel):
    id_evento: Optional[int] = None
    titulo: str
    descripcion: Optional[str] = None
    fecha: datetime
    id_categoria: int
    id_ubicacion: int
    id_organizador: int

    @field_validator('titulo')
    @classmethod
    def validar_titulo(cls, value: str):
        if not value or not value.strip():
            raise ValueError('El título del evento es obligatorio')
        return value.strip()

    class Config:
        from_attributes = True