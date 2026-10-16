from fastapi import APIRouter
from app.models.ubicacion import UbicacionBase
from app.repositories.ubicacion_repo import UbicacionRepository

router = APIRouter(prefix="/ubicaciones", tags=["Ubicaciones"])

@router.post("/")
def crear_ubicacion(data: UbicacionBase):
    return {"id_ubicacion": UbicacionRepository.crear(data)}