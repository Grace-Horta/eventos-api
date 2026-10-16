from pydantic import BaseModel, field_validator
from typing import Optional

class InscripcionBase(BaseModel):
    id_inscripcion: Optional[int] = None
    id_estudiante: int
    id_evento: int

    @field_validator('id_estudiante', 'id_evento')
    @classmethod
    def validar_ids(cls, value: int):
        if value <= 0:
            raise ValueError('Los identificadores deben ser enteros positivos')
        return value

    class Config:
        from_attributes = True