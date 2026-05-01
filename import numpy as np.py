"""Practica 4"""

import os
import numpy as np
import sklearn.tree import DecisionTreeClassifier

# Simulación de datos

"""
<<<<<<< HEAD
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
=======
Caracteristicas: [Tiempo_respuesta_ms]
"""

x = np.array([10], [20], [30], [200], [300], [400])
y = np.array([1, 1 ,1 , 0, 0, 0])

"""
Modelo de IA
"""

modelo = DecisionTreeClassifier
modelo.fit(X,y)

"""
Escaneo de red
"""

red = "192.168.1"

for i in range (1,20):
    ip = red + str(i)

    """
    Ping window
    """

    respuesta = os.popen(f"ping -n -w 100 {ip}").read()

    if "tiempo=" in respuesta:

        try:
            tiempo = int(respuesta.split("tiempo=") [1].split ("ms") [0])

        except:
            tiempo = 300

    else:
        tiempo = 400

    """
    Predicción con IA
    """
    
    prediccion = modelo.predict([[tiempo]]) [0]
    
    prediccion = modelo.predict([[tiempo]])

    if predicci == 1:
        print(f"Dispositivo Activa IA {ip} - {tiempo} ms")

    else:
        print(f"Dispositivo Inactivo (IA): {ip}")

        
>>>>>>> 17c6e38ff28840ffecccbaeb8cd5b4d84e509995
