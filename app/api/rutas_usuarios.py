from fastapi import APIRouter
from app.models.usuario import UsuarioBase
from app.repositories.usuario_repo import UsuarioRepository

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/")
def crear_usuario(data: UsuarioBase):
    return {"id_usuario": UsuarioRepository.crear(data)}