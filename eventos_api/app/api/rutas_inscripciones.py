from fastapi import APIRouter
from app.models.inscripcion import InscripcionBase
from app.repositories.inscripcion_repo import InscripcionRepository

router = APIRouter(prefix="/inscripciones", tags=["Inscripciones"])

@router.post("/")
def crear_inscripcion(data: InscripcionBase):
    return {"id_inscripcion": InscripcionRepository.crear(data)}