from sqlalchemy.orm import Session
from app.models.calificacion import Calificacion
from app.schemas.calificacion import CalificacionCreate

def crear_calificacion(db: Session, data: CalificacionCreate):

    nueva = Calificacion(
        nombre=data.nombre,
        materia=data.materia,
        calificacion=data.calificacion
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


def obtener_calificaciones(db: Session):
    return db.query(Calificacion).all()