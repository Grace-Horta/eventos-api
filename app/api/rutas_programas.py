from fastapi import APIRouter
from app.models.programa import ProgramaBase
from app.repositories.programa_repo import ProgramaRepository

router = APIRouter(prefix="/programas", tags=["Programas"])

@router.post("/")
def crear_programa(data: ProgramaBase):
    return {"id_programa": ProgramaRepository.crear(data)}