"""
Sistema de tráfico de datos con IA 
"""


import numpy as np
import pandas as pd
import random 
import time
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


"""
Generar Datset
"""

def generar_datos (n=1000):
    np.random.seed(42)

    data = pd.DataFrame({   
        "paquetes": np.random.randint(100,5000, n),
        "bytes": np.random.randint(1000, 60000, n),
        "duración": np.random.uniform(0.1, 15, n),
        "protocolo": np.random.choice([0,1], n),
    })


    condiciones = [
        (data["bytes"] > 45000),
        (data["paquetes"] < 2000),


    ]

    opciones = ["ataque", "video"]

    data["tipo"] = np.select(condiciones, opciones, default="normal")

    return data

"""
Entrenamiento del modelo
"""


def entrenar_modelo(data): 
    x = data[["paquetes", "bytes", "duración", "protocolo"]]
    y =data["tipo"]

    X_train, X_test, y_train, y_test, = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    modelo = RandomForestClassifier(n_estimators=100)
    modelo.fit(X_train, y_train)


    prediciones = modelo.predict(X_test)

    print("\n Evaluación del modelo:")
    print("Accuracy:", accuracy_score(y_test, prediciones))
    print("\n Reporte:\n", classification_report(y_test, prediciones))

    return modelo

""" 
Simulación en tiempo real
"""

def simulacion_tiempo_real(modelo, iteraciones=10):
    print("\n Iniciando la simulación en tiempo real...\n")

    for i in range(iteraciones):
        paquetes = random.radint(100, 5000)
        bytes_ = random.randint(1000, 60000)
        duración = random.uniforme(0.1, 15)
        protocolo = random.choice([0,1], 1)

        muestra = np.array([paquetes, bytes_, duración, protocolo])
        pred = modelo.predict(muestra)[0]

        print(f"Iteración {i+1}")
        print(f"Paquetes: {paquetes}, Bytes: {bytes_}, Duración: {duración:.2f}, Protocolo {protocolo}")
        print(f"Clasificación: {pred}")
        print("-" * 50)

        time.sleep(1)

"""
Gráficas
"""


def graficas(data):
    plt.figure()
    plt.hist(data["bytes"])
    plt.title("Distribución de Bytes")
    plt.xlabel("Bytes")
    plt.ylabel("Frecuencia")
    plt.grid()
    plt.show()

    plt.figure()
    plt.hist(data["paquetes"])
    plt.title("Distribución de Paquetes")
    plt.xlabel("Paquetes")
    plt.ylabel("Frecuencia")
    plt.grid()
    plt.show()

    plt.figure()
    data["tipo"].value_counts().plot(kind ='bar')
    plt.title("Tipos de Tráfico")
    plt.xlabel("Tipo")
    plt.ylabel("Cantidad")
    plt.grid()
    plt.show()

"""
Main
"""
if __name__ == "__main__":
    data = generar_datos(1000)
    print("Dataset generado: ")
    print(data.head())

    modelo = entrenar_modelo(data)

    graficas(data)

    simulacion_tiempo_real(modelo, iteraciones=10)