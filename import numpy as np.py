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
paquetes_enviados = []
paquetes_recibidos = []
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
    Latencias.append(tiempo_recepcion - tiempo_envio)
    paquetes_enviados.append(Tamano_paquete)
    paquetes_recibidos.append(Tamano_paquete)

    """
    Metricas
    """

    total_enviados = len(paquetes_enviados)
    total_recibidos = len(paquetes_recibidos)
    tasa_perdida = perdidos / Num_paquetes 
    
    latencia_promedio = np.mean(latencia)

    throughput = (sum(paquetes_recibidos) / sum (Latencias)) if Latencias else 0

    """
    Configuración de resultados
    """

    print(f"Paquetes enviados: {total_enviados}")
    print(f"Paquetes recibidos: {total_recibidos}")
    print(f"Paquetes perdida: {perdidos}")
    print(f"Tasa de perdidad: {tasa_perdida:.2f}")
    print(f"Latencia promedio: {latencia_promedio:.4f}")
    print(f"Throughput: {throughput:.2f} bytes/s")

    """Grafica de latencias"""

    plt.plot(Latencias)
    plt.title("Latencia por paquete")
    plt.xlabel("Paquetes")
    plt.ylabel("Latencia(s)")
    plt.grid()
    plt.show()

    
