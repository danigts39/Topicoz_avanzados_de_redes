import numpy as np
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

"""
Dataset
"""

def generar_datos(n=2000):
    np.random.seed(42)

    data = pd.DataFrame({
        "paquetes": np.random.randint(100, 5000, n),
        "bytes": np.random.randint(1000, 60000, n),
        "duración": np.random.uniform(0.1, 15, n),
        "protocolo": np.random.choice([0, 1], n),
        "latencia": np.random.randint(1, 200, n),
        "puerto": np.random.randint(20, 9000, n),
        "perdida": np.random.uniform(0, 10, n),
        "jitter": np.random.uniform(0, 50, n),
    
    })

    condiciones = [
        (data ["bytes"]> 45000  ), (data ["jitter"] > 40),
        (data ["paquetes"]> 15000), (data ["jitter"] > 20 ),

        ]
    
    opciones = ["ataque", "ataque","video", "video"]

    data["tipo"] = np.select(condiciones, opciones, default = "normal")

    return data





df = generar_datos()

fig = px.scatter_3d(
    df,
    x="bytes",
    y="paquetes",
    z="latencia",
    color="tipo",
    title="Visualización 3D interactiva del tráfico de red",
    opacity=0.7
)

fig.show()