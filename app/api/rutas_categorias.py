from fastapi import APIRouter
from app.models.categoria import CategoriaBase
from app.repositories.categoria_repo import CategoriaRepository

router = APIRouter(prefix="/categorias", tags=["Categorías"])

@router.post("/")
def crear_categoria(data: CategoriaBase):
    return {"id_categoria": CategoriaRepository.crear(data)}