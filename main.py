from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import statistics

app = FastAPI(title="Servidor Inteligente de Calificación")

"""
Base de datos (SQLite)
"""

def get_db():
    return sqlite3.connect("umb.db")

def crear_tabla():
    conn = get_db()
    cursor = conn.cursor()

    # Tabla estudiantes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    """)

    # Tabla calificaciones
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

crear_tabla()

"""
Modelos
"""

class Estudiante(BaseModel):
    nombre: str

class Calificacion(BaseModel):
    estudiante_id: int
    materia: str
    nota: float

"""
IA Simple
"""

def evaluar_desempeno(notas):
    if len(notas) == 0:
        return {"error": "Sin calificaciones"}
    
    promedio = statistics.mean(notas)

    if promedio >= 9:
        estado = "Excelente"
        recomendacion = "Puede participar en proyectos"
    elif promedio >= 7:
        estado = "Regular"
        recomendacion = "Debe reforzar algunos temas"
    else:
        estado = "En riesgo"
        recomendacion = "Requiere tutorías"

    return {
        "promedio": round(promedio, 2),
        "estado": estado,
        "recomendacion": recomendacion
    }

"""
Endpoints
"""

"""@app.get("/")
def inicio():
    return {"mensaje": "Servidor Inteligente de calificaciones"}"""

@app.get("/")
def inicio():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()

    cursor.execute("SELECT * FROM calificaciones")
    calificaciones = cursor.fetchall()

    conn.close()

    return {
        "mensaje": "Servidor Inteligente de calificaciones",
        "estudiantes": estudiantes,
        "calificaciones": calificaciones
    }

# Crear estudiante
@app.post("/estudiantes/")
def agregar_estudiante(estudiante: Estudiante):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO estudiantes (nombre) VALUES (?)",
        (estudiante.nombre,)
    )

    conn.commit()
    conn.close()

    return {"mensaje": "Estudiante agregado"}

# Ver estudiantes
@app.get("/estudiantes/")
def obtener_estudiantes():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()

    conn.close()

    return estudiantes

# Agregar calificación
@app.post("/calificaciones/")
def agregar_calificacion(calificacion: Calificacion):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO calificaciones (estudiante_id, materia, nota)
        VALUES (?, ?, ?)
    """, (calificacion.estudiante_id, calificacion.materia, calificacion.nota))

    conn.commit()
    conn.close()

    return {"mensaje": "Calificación agregada"}

# Evaluar estudiante
@app.get("/evaluar/{estudiante_id}")
def evaluar_estudiante(estudiante_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nota FROM calificaciones
        WHERE estudiante_id = ?
    """, (estudiante_id,))

    notas = [row[0] for row in cursor.fetchall()]

    conn.close()

    return evaluar_desempeno(notas)