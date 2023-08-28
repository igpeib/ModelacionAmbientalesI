# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 18:13:55 2023

@author: igorp
"""

# comp_prueba00.py 
# Programa para simular el ejemplo de población
#del Capítulo 3 de Ford
# 
import numpy as np, matplotlib.pyplot as plt
# ------ parámetros 
tasa_A = 0.1    # 10% / año tasa de avejentamiento
tasa_MD= 0.1    # 10% /año tasa pocentual de maduración
tasa_M= 0.2     # 20%/año tasa porcentual de mortalidad   
fraccion_hembras = 0.5
nacimientos_hembra_año = 0.5
DeltaT = 1    # Delta t = 1 año
Tmax =100      # simulación hasta este año
##---- despliega parámetros
print('tasa porcentual avejentamiento', tasa_A)
print('tasa pocentual de maduración', tasa_MD)
print('tasa porcentual de mortalidad', tasa_M)
# INICIALIZACIÓN DE VARIABLES
jovenes = 50e6
maduros = 30e6
ancianos = 20e6
### imprime valores iniciales 
print('jovenes=',jovenes)
print('maduros=',maduros)
print('ancianos=',ancianos)
print('población total=', jovenes+ancianos+maduros)
#-------------------------
# Listas para guardar datos
jovenesList=[]
madurosList=[]
ancianosList=[]
poblaciontotalList=[]
xValues=[]
#---------------------------
for n in range(1,Tmax+1):
    print("n=" ,n)
    jovenesLast = jovenes
    madurosLast = maduros
    ancianosLast = ancianos
    jovenes = jovenesLast - (DeltaT*tasa_MD*jovenesLast) + (DeltaT * nacimientos_hembra_año* fraccion_hembras* madurosLast)
    maduros = madurosLast - (DeltaT*tasa_A*madurosLast) + (DeltaT*tasa_MD*jovenesLast)
    ancianos = ancianosLast - (DeltaT*tasa_M*ancianosLast) + (DeltaT*tasa_A*madurosLast)
    #--------------------------
    # guarda en listas:
    xValues.append(n)
    jovenesList.append(jovenes)
    madurosList.append(maduros)
    ancianosList.append(ancianos)
    poblaciontotalList.append(jovenes+ancianos+maduros)
    ### imprime valores 
    print('jovenes=',jovenes)
    print('maduros=',maduros)
    print('ancianos=',ancianos)
    print('población total=', jovenes+ancianos+maduros)
#num_points = 450
#x_min, x_max = 0, 4
#x_values = np.linspace(1, Tmax+1)
#y_values = x_values**2
plt.plot(xValues, jovenesList,xValues,madurosList, xValues, ancianosList)
plt.xlabel('tiempo')
plt.plot(xValues,poblaciontotalList)
#plt.show()