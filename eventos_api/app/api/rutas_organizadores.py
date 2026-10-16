from fastapi import APIRouter
from app.models.organizador import OrganizadorBase
from app.repositories.organizador_repo import OrganizadorRepository

router = APIRouter(prefix="/organizadores", tags=["Organizadores"])

@router.post("/")
def crear_organizador(data: OrganizadorBase):
    return {"id_organizador": OrganizadorRepository.crear(data)}