from pydantic import BaseModel, field_validator
from typing import Optional

class AsistenciaBase(BaseModel):
    id_asistencia: Optional[int] = None
    asistio: bool = True
    id_inscripcion: int

    @field_validator('id_inscripcion')
    @classmethod
    def validar_inscripcion(cls, value: int):
        if value <= 0:
            raise ValueError('El ID de inscripción no es válido')
        return value

    class Config:
        from_attributes = True