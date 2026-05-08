from pydantic import BaseModel

class CalificacionCreate(BaseModel):
    alumno: str
    materia: str
    calificacion: float


class CalificacionResponse(CalificacionCreate):
    id: int


    class Config:
        orm_mode = True