from fastapi import APIRouter
from app.models.asistencia import AsistenciaBase
from app.repositories.asistencia_repo import AsistenciaRepository

router = APIRouter(prefix="/asistencia", tags=["Asistencia"])

@router.post("/")
def registrar_asistencia(data: AsistenciaBase):
    return {"id_asistencia": AsistenciaRepository.crear(data)}