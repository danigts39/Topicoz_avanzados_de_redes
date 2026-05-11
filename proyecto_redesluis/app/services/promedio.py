def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0

    total = sum(c.calificacion for c in calificaciones)
    return total / len(calificaciones)