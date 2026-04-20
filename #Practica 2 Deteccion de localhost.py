#Practica 2 Deteccion de localhost

from scapy.all import ARP, Ether, srp, sniff
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


"""
Escaneo de red
"""

def escanear_red(ip_range="192.168.1.1/24"):
    print("Escaneando dispositivos....")

    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    paquete = ether /arp

    resultado = srp(paquete, timeout=2, verbose=0) [0]

    dispositivos = []
    for enviado, recibido in resultado:
        dispositivos.append({
            "ip": recibido.prsc,
            "mac": recibido.hwsrc
        })

        return dispositivos
    
"""
Captura de tráfico
"""

trafico = []

def capturar_paquetes(packet):
    if packet.haslayer("IP"):
        trafico.append({
            "ip": packet["IP"].scr,
            "longitud": len(packet),
            "protocolo": packet["IP"].proto
        })

def analizar_practico(tiempo=10):
    print("Capturando trafico...")
    sniff(prn=capturar_paquetes, timeout=tiempo)
    return pd.DataFrame(trafico)

import os
import numpy as np
import sklearn 
from sklearn.tree import DecisionTreeClassifier

"""caracteristicas:[Tiempo_respuesta_ms]"""

x=np.array([[10],[20],[200],[300],[400]])
y=np.array([1,1,1,0,0])

"""modelo de ia"""
modelo=DecisionTreeClassifier()
modelo.fit(x,y)

"""escaner de red"""
red = "192.168.1."
for i in range(1,20):
    ip = red + str(i)
    
    """ping window"""
    respuesta = os.popen("ping -n -w 100 {ip}").read()
    
    if "tiempo=" in respuesta:
        
        try:
            tiempo = int(respuesta.split("tiempo=")[1].split("ms")[0])
        except:
            tiempo =400
    else:
        tiempo = 400
        
    """prediccion del modelo"""
    prediccion = modelo.predict([[tiempo]])[0]
    
    if prediccion == 1:
       print(f"Dispositivo Activa IA: {ip} - {tiempo} ms")
    else:
       print(f"Dispositivo Inactivo (IA): {ip}")