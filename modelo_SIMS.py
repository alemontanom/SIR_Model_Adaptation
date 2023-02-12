# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:04:34 2022

@author: alemontanom
"""

import scipy.integrate as spi
import pylab as pl
import numpy as np
N = 120000000 #poblacion total inicial
m = 0.05 #tasa de mortalidad
i =0.143500111930087#tasa de infección con R0=2.009
r = 0.071428571428571 #tasa de recuperación, 1/14
e = 0.014 #tasa para medir el tiempo que tarda alguien en pasar de recuperado a susceptible nuevamente, considerando dos meses y cachito
TS=1.0 #medida del tiempo, se refiere a 1 día
ND= 290 #cantidad de medidas de tiempo, en este caso ND días
I0= 93 / N  #cantidad inicial de infectados normalizada, o sea I(0) entre la poblacion
S0= 1 - I0 #susceptibles iniciales, poblacion total menos infectados iniciales
R0 = 0 #recuperados iniciales 
M0 = 0 #muertos iniciales
INPUT = (S0, I0, M0, R0) 

def SIMS(INP,t):  #parametros de la funcion: INP=lista con los valores iniciales de S, I y R, t = el rango de tiempo que modelara la simulacion
      '''las ecuaciones:'''
      Y=np.zeros((4)) #te regresa un array, un vector, de tamaño 4 con puros ceros en sus entradas
      V = INP#asi, V[0]=S0, V[1]=I0, V[2]=M0, V[3]=R0
      Y[0] = - i * V[0] * V[1] + e * V[3] #susceptibles, le quite la resta de los muertos
      Y[1] = i * V[0] * V[1] - r * V[1] - m * V[1] #infectados
      Y[2] = m * V[1] #muertos
      Y[3] = r*V[1] - e*V[3] #recuperados que todavía no son susceptibles otra vez, en el momento t
      return Y   # For odeint que es una funcion ya incluida en python



t_start = 0.0; t_end = ND; t_inc = TS #usa la medida TS y la cantidad de medidad ND para determinar cuánto tiempo correrá
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(SIMS,INPUT,t_range) #llama a la función con odeint, que es un integrador de python para sisteas de ecuaciones diferenciales ordinarias y dándole de parámetros los S0, I0 y R0 en INPUTy el tiempo que correrá en t_range 

print (RES) # RES = susceptibles, infectados, muertos, recuperados en el momento 

#Graficas:
pl.subplot(311)
pl.plot(RES[:,0], '-b', RES[:,1], '-m',  RES[:,2], '-r', RES[:,3], '-c') 
pl.title('Comportamiento Modelo SIMS')
pl.xlabel('Time')
pl.ylabel('Población')
pl.show()

pl.subplot(311)
pl.plot(RES[:,0], '-b', label='Susceptibles')
pl.title('Comportamiento modelo SIMS')
pl.xlabel('Time')
pl.ylabel('Susceptibles')
pl.subplot(312)
pl.plot(RES[:,1], '-m', label='Infectados')
pl.xlabel('Time')
pl.ylabel('Infectados')
pl.subplot(313)
pl.plot(RES[:,2], '-r', label='Muertos acumulados')
pl.xlabel('Time')
pl.ylabel('Muertos')
pl.show()

pl.subplot(311)
pl.plot(RES[:,3], '-c', label='Recuperados no susceptibles')
pl.xlabel('Time')
pl.ylabel('Recuperados no susceptibles')
pl.show()

print(RES[-1])
