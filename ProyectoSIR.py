#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:00:34 2022

Proyecto final Mate Compu

@author: alemontano
"""

"""suceptibles iniciales = poblacion 
poblacion n = suceptibles n (suceptibles n-1 + recuperados) + infectados - muertos

tasa de infectados 
"""
M_orig = 1000 #muertes totales reales 
n = 10

def ajusteTasaInfeccion (m, i, S, I) :# (entrada = muertos calculados): 
    while () : 
        if (m < 0.95 * M_orig):
            i = i*1.01
            SIMS(muertos(i, S), i, S, I, n)
        elif (m < 01.05 * M_orig):
            i = i * 0.99
            SIMS(muertos(i, S), i, S, I, n)
        else:
            break 
    return i


def SIMS(M, I, i, S, n): #i = tasa infeccion, r = tasa recuperacion, mu = tasa muerte, n = dias de modelo
    r=1.30
    M, invN = 0, 1/(S+I)
    for i in range (n):
        S, I, M = S - i*S*I*invN + r*I, I + I*i*S*invN- muertos (i) - r*I, muertos(i) #M+mu*I, I = I + i*S*I*invN - -r*I - mu*I
    return M, i, S, I 

        
def muertos (i, S):
    I = i*S
    m1 = I*0.005*0.2601
    m2 = I*0.002*0.1697
    m3 = I*0.006*0.4106
    m4 = I*0.0829*0.0245
    m5 = I*0.0767*0.088
    return m1+m2+m3+m4+m5
    #división por edades con la piramide poblacionar --> *pesos = proba de morir del grupo--> los sumas todso
    
    
"""def hospitalizacion (infectados):
    #dependiendo del rango de edad determinará la probabilidad de necesitar hospitalización
    #entradas = infectados, se dividirá por la piramide de edad en mexico 
    #pesos = probabilidad de necesitar hospitalizacion dependiendo del rango socioeconomico, tambien estaran en una lista 
    #salida = cantidad de gente que necesitó hospitalizacion 
    pass
    

def rangoSocioEconomico (hospital):
    #de los que necesitaron hospitalización, determinará cuantos mueren según el rango socioeconómico 
    #entradas = cantidad de gente que necesitó hospitalizacion 
    #dividida por los porcentajes de personas por rango socioeconomico en Mexico 
    # pesos = `probabilidad de muerte dependiendo del rango socioeconomico (por falta de acceso a servicios de salud)
    #salida = cantidad de gente muerta 
    pass
    


graficar el comportamiento de las distintas simulaciones"""