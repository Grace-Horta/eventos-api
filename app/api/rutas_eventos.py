from fastapi import APIRouter
from app.models.evento import EventoBase
from app.repositories.evento_repo import EventoRepository

router = APIRouter(prefix="/eventos", tags=["Eventos"])

@router.post("/")
def crear_evento(data: EventoBase):
    return {"id_evento": EventoRepository.crear(data)}