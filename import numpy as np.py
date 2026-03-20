import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

"""
configuración
"""

Num_paquetes = 100
Tamano_paquete = 1024 #bytes
velocidad_red = 100000 #bytes por segundo

"""
Listas para almacenar los datos

"""
Latencias = []
paquetas_enviados = []
paquetas_recibidos = []
perdidos = 0

print("Simulando tráfico de datos ....\n ")

for i in range (Num_paquetes):
    tiempo_envio = time.time()
    """
    Simular latencia (entre 10n y 100 ns)
    """
    latencia = random.uniform(0.01, 0.1)
    time.sleep(latencia)

    """
    Simular perdida de paquetes (10% de probabilidad)
    """

    if random.random() < 0.1:
        perdidos += 1
        continue

    tiempo_recepcion = time.time()
    latencia.append(tiempo_recepcion - tiempo_envio)
    paquetas_enviados.append(Tamano_paquete)
    paquetas_recibidos.append(Tamano_paquete)

    """
    Metricas
    """

    total_enviados = len(paquetas_enviados)
    total_recibidos = len(paquetas_recibidos)
    tasa_perdida = perdidos / Num_paquetes 
    
    latencia_promedio = np.mean(latencias)

    throughput = (sum(paquetas_recibidos) / sum (latencia)) if latencias else 0


        

