"""Practica 4"""

import os
import numpy as np
import sklearn.tree import DecisionTreeClassifier

# Simulación de datos

"""
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

        