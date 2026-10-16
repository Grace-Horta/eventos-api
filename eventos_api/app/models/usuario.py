from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UsuarioBase(BaseModel):
    id_usuario: Optional[int] = None
    nombre: str
    apellido: str
    documento_identidad: str
    telefono: Optional[str] = None
    email: EmailStr
    password: str
    estado:str

    '''
    semestre: int
    id_rol: int
    id_programa: int

    @field_validator('nombre', 'apellido')
    @classmethod
    def validar_texto(cls, value: str):
        if not value or not value.strip():
            raise ValueError('El campo no puede estar vacío')
        return value.strip()

    @field_validator('semestre')
    @classmethod
    def validar_semestre(cls, value: int):
        if value < 1 or value > 16:
            raise ValueError('El semestre debe ser un número entre 1 y 16')
        return value

    class Config:
        from_attributes = True

        '''