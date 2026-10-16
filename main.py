from fastapi import FastAPI
from app.api import (
    rutas_roles,
    rutas_modelos,
    rutas_modelos_x_rol,
    rutas_facultades,
    rutas_programas,
    rutas_ubicaciones,
    rutas_usuarios,
    rutas_estudiantes,
    rutas_organizadores,
    rutas_categorias,
    rutas_eventos,
    rutas_inscripciones,
    rutas_asistencia,
    rutas_certificados,
)

app = FastAPI(
    title="API de Gestión de Eventos Académicos y Extracurriculares",
    description="Backend modular para la administración de eventos e inscripciones",
    version="1.0.0"
)

# Registro de rutas de los 14 módulos
app.include_router(rutas_roles.router)
app.include_router(rutas_modelos.router)
app.include_router(rutas_modelos_x_rol.router)
app.include_router(rutas_facultades.router)
app.include_router(rutas_programas.router)
app.include_router(rutas_ubicaciones.router)
app.include_router(rutas_usuarios.router)
app.include_router(rutas_estudiantes.router)
app.include_router(rutas_organizadores.router)
app.include_router(rutas_categorias.router)
app.include_router(rutas_eventos.router)
app.include_router(rutas_inscripciones.router)
app.include_router(rutas_asistencia.router)
app.include_router(rutas_certificados.router)

@app.get("/")
def estado_api():
    return {"mensaje": "La API de Gestión de Eventos está activa"}