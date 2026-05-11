from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal, engine, Base

from app.schemas.calificacion import (
    CalificacionCreate,
    CalificacionResponse
)

from app.crud.calificacion import (
    crear_calificacion,
    obtener_calificaciones
)

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Conexión a DB
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Crear calificación
@app.post(
    "/calificaciones/",
    response_model=CalificacionResponse
)
def crear(
    data: CalificacionCreate,
    db: Session = Depends(get_db)
):
    return crear_calificacion(db, data)


# Obtener calificaciones
@app.get(
    "/calificaciones/",
    response_model=list[CalificacionResponse]
)
def listar(
    db: Session = Depends(get_db)
):
    return obtener_calificaciones(db)

from app.core.database import (
    SessionLocal,
    engine,
    Base
)

Base.metadata.create_all(bind=engine)