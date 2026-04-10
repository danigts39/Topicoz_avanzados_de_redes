"""
Sistema de tráfico de datos con IA EXAMEN
Librerias a usar para que el programa funcione
"""

import numpy as np
import pandas as pd
import random
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.svm import SVC
import matplotlib.pyplot as plt




"""
Aqui se genera el data set el cual contiene las metricas para num paquetes, tamaño de datos (bytes), tiempo de transmisión
tipoi de transmisión, tipo de tráfico, latencia y ancho de banda
"""

def generar_datos(n=1000):
    np.random.seed(42)

    data = pd.DataFrame({
        "paquetes": np.random.randint(100, 5000, n),
        "bytes": np.random.randint(1000, 60000, n),
        "duracion": np.random.uniform(0.1, 15, n),
        "latencia": np.random.randint(1, 200, n),
        "puerto": np.random.randint(20, 9000, n),
        "perdida": np.random.uniform(0, 10, n),
        "jitter": np.random.uniform(0, 50, n),
        "ancho_banda": np.random.uniform(1, 100, n),
        "protocolo": np.random.choice([0, 1], n),
    })

    
    condiciones = [
        (data["bytes"] > 58000) | (data["perdida"] > 8),
        (data["latencia"] > 120), 
        (data["ancho_banda"] < 10),
    ]

    opciones = ["ataque", "normal","video"]

    data["tipo"] = np.select(condiciones, opciones, default="normal")

    return data


"""
Entrenaniento del modelo, Es el cómo el algoritmo piensa y determina que es un ataque y denomina otros datos importantes como los resultados que se muestran, la precisión del algoritmo, la matriz de confusión y el reporte
"""

def entrenar_modelo(data):

    X = data[[
    "paquetes","bytes","duracion","latencia","puerto","perdida","jitter", "ancho_banda",  "protocolo" ]]
    y = data["tipo"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    pred = modelo.predict(X_test)

    print("\nResultados se muestran a continuación")
    print("Accuracy:", accuracy_score(y_test, pred))
    print("\nMatriz de confusión:\n", confusion_matrix(y_test, pred))
    print("\nReporte:\n", classification_report(y_test, pred))

    return modelo


"""
Simulación en tiempo real, es la simulación ya activa que muestra que datos son considerados ataques y que datos son considerados normales
"""

def simulacion_tiempo_real(modelo, iteraciones=10):
    print("\n Iniciando la simulación en tiempo real...\n")

    for i in range(iteraciones):

        paquetes = random.randint(100, 5000)
        bytes_ = random.randint(1000, 60000)
        duracion = random.uniform(0.1, 15)
        latencia = random.randint(1, 200)
        puerto = random.randint(20, 9000)
        perdida = random.uniform(0, 10)
        jitter = random.uniform(0, 50)
        ancho_banda = random.uniform(1, 100)
        protocolo = random.choice([0, 1])

        muestra = np.array([[paquetes, bytes_, duracion, latencia,puerto, perdida, jitter, ancho_banda, protocolo]])
        pred = modelo.predict(muestra)[0]

        print(f"Iteración {i+1}")
        print(f"Paquetes: {paquetes}, Bytes: {bytes_}, Duración: {duracion:.2f}, Protocolo {protocolo}")
        print(f"Clasificación: {pred}")
        print("-" * 50)

        time.sleep(1)


"""
Graficas, la visualización de los resultados en tiempo real
"""

def graficas(data):

    plt.figure()
    plt.hist(data["bytes"], bins=30)
    plt.title("Distribución de Bytes")
    plt.grid()
    plt.show()

    plt.figure()
    plt.hist(data["latencia"], bins=30)
    plt.title("Distribución de Latencia")
    plt.grid()
    plt.show()

    plt.figure()
    data["tipo"].value_counts().plot(kind="bar")
    plt.title("Tipos de tráfico (ataque / video / normal)")
    plt.grid()
    plt.show()


"""
Main
"""

if __name__ == "__main__":
    data = generar_datos(2000)
    print("Dataset generado:")
    print(data.head())

    modelo = entrenar_modelo(data)

    graficas(data)

    simulacion_tiempo_real(modelo, iteraciones=10)
