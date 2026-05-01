"""Practica3parcial2"""

from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import statistics
import sqlite3 
app = FastAPI(title="Servidor Inteligente de calificaciones")

"""
BASE DE DATOS
"""
def get_db():
    conn = sqlite3.connect("escuela.db")
    return conn

def crear_tablas():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calificaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        estudiante_id INTEGER,
        materia TEXT,
        nota REAL,
        FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id)
    )
    """)

    conn.commit()
    conn.close()

crear_tablas()

# ------------------------
# MODELOS
# ------------------------
class
"""
Modelos
"""
class Calificacion(BaseModel):
    materia: str
    
class Estudiante(BaseModel):
    nombre: str
    calificacion: List[Calificacion]
    nota: float

"""
Base de datos simulada
"""
db = []

"""
Funcion de IA simple
"""

def evaluar_desempeno(notas):
    promedio = statistics.mean(notas)

    if promedio >= 9:
        estado ="Excelente"
        recomendacion = "Puedes participar en proyecto"

    elif promedio >= 7:
        estado = "Regular"
        recomendacion = "Necesitas reforzar algunos temas"
    else:
        estado = "En riesgo"
        recomendacion = "Requiere tutorias urgentes y seguimiento"

    return {
        "promedio": promedio,
        "estado": estado,
        "recomendacion": recomendacion
    }


"""
Endpoints
"""

@app.get("/")
def inicio():
    return {"mensaje" : "Servidor Inteligente de calificaciones"}

@app.post("/estudiantes/")
def agregar_estudiantes(estudiante: Estudiante):
    db.append(estudiante)
    return {"mensaje" : "Estudiante agregado"}

@app.get("//")