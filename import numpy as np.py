import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

"""
Configuracion

"""
Num_paquetes=100
Tam_paquetes=1024 #Bytes
Velocidad_red=100000 #bytes por segundo

"""
Lista para almacenar datos
"""

latencias=[]
paquetes_enviados=[]
paquetes_recibidos=[]
perdidos=0

print("simulando trafico de datos")

for i in range (Num_paquetes):
    tiempo_envio=time.time()

    """
    Simular latencia (entre 10ns y 100ns)
    """
    latencia=random.uniform(0.01,0.1)
    time.sleep(latencia)

    """
    Simular perdida de paquetes (10%)
    """
    if random.random() < 0.1:
        perdidos += 1
        continue

    tiempo_recepcion = time.time()
    latencias.append(tiempo_recepcion - tiempo_envio)
    paquetes_enviados.append(Tam_paquetes)
    paquetes_recibidos.append(Tam_paquetes)

"""
Metricas
"""
total_enviados = len(paquetes_enviados)
total_recibidos = len(paquetes_recibidos)
tasa_perdida = perdidos/Num_paquetes

latencia_promedio = np.mean(latencias)
throughput = (sum(paquetes_recibidos)/sum(latencias)) if latencias else 0

"""
Configuracion de resultados
"""
print(f"paquetes enviados: {total_enviados}")
print(f"paquetes recibidos: {total_recibidos}")
print(f"paquetes perdidos: {perdidos}")
print(f"tasa de perdida: {tasa_perdida}")
print(f"throughput: {throughput:.2f} bytes/s")

"""
Grafica de latencias
"""
plt.plot(latencias)
plt.title("latencia por paquete")
plt.xlabel("paquetes")
plt.ylabel("latencia(s)")
plt.grid()
plt.show()