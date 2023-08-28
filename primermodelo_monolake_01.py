# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 18:13:55 2023

@author: igorp
"""

#   primermodelo_monolake_01.py 
#   Hace la simulación del primer modelo de volumen de agua en el Lago Mono
#   del Capítulo 3 de Ford. Este es el modelo más simple con todos 
#   los parámetros fijos 
# ---- INICIO
import numpy as np, matplotlib.pyplot as plt
# ------ parámetros
area_superficial = 39       # [kilo acres] área superficial del lago
tasa_evaporacion = 3.75     # [ft/yr] se ajusta según salinidad
tasa_precipitacion = 0.667  # [ft/yr]
# ----  parámetros que definen el flujo hacia el lago
# ----  después de la desviación:
extraccion = 100            # [KAF] Kilo acres-pie     
escurrimiento_medido = 150  # [KAF] Kilo acres-pie
# --------------  Flujos de entrada:
otros_entrada = 47.6        # [KAF/yr] otros flujos de entrada
flujo_entrada_postdesviacion = escurrimiento_medido - extraccion  
precipitacion = area_superficial*tasa_precipitacion
# ---------------  Flujos de salida
otros_salida = 33.6        # [KAF/yr]
evaporacion = area_superficial * tasa_evaporacion 
##---- despliega parámetros
print('área superficial inicial', area_superficial)
print('tasa de evaporación', tasa_evaporacion)
print('tasa de precipitación', tasa_precipitacion)
print('No se despliegan otros parámetros')
print('====================================================')
##----------------------------------
# INICIALIZACION DE VARIABLES
agua_lago = 2228.0  # [KAF] total agua inicial en lago en 1990
anio = 1990  
# En esta simulación esa es la única variable que evolucionamos
# ---- DELTA T Y TIEMPO MÁXIMO DE LA SIMULACIÓN
DeltaT = 1    # Delta t = 1 año
Tmax =2031 # simulación hasta este año
### --- imprime valores iniciales 
print('volumen de agua inicial en lago [KAF]',agua_lago)
#-------------------------
# Crear listas para guardar datos se ponen los datos iniciales
agua_lagoList=[agua_lago] 
anioList=[anio] #aquí vamos a guardar los años para graficar
#-----Evolución temporal-
while anio<Tmax:
    #agua_lagoLast = agua_lago
    agua_lago= agua_lago + DeltaT*(flujo_entrada_postdesviacion + precipitacion + otros_entrada) -DeltaT*(evaporacion+otros_salida)
    anio += 1
    #--------------------------
    # guarda en listas:
    agua_lagoList.append(agua_lago)
    anioList.append(anio)
### ------
### imprime valores  dentro del loop 
    print('año=', anio)
    print('volumen de agua en el lago=',agua_lago)
# # ------- Grafica resultado
plt.plot(anioList, agua_lagoList)
# plt.xlabel('tiempo')
#plt.plot(xValues,poblaciontotalList)