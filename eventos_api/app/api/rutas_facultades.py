from fastapi import APIRouter
from app.models.facultad import FacultadBase
from app.repositories.facultad_repo import FacultadRepository

router = APIRouter(prefix="/facultades", tags=["Facultades"])

@router.post("/")
def crear_facultad(data: FacultadBase):
    return {"id_facultad": FacultadRepository.crear(data)}