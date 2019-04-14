# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:43:48 2019

@author: Tiago e Guilherme
"""
import matplotlib.pyplot as plt
import numpy as np

class ex3:
    
    """
    Função que aproxima o valor de yk de y para a EDO fornecida utilizando o método de Euler explícito.
    """
    def EE(delta, n):
        y0 = delta
        h = 2 / (delta * n)     #h = Tamanho do passo: (2/delta - 0)/n
        t = 0
        z =[]       #Lista para os valores de Yk
        x = []      #Lista para os valores de t
        x.append(t)
        z.append(y0)
        for i in range(1, n):
            y1 = y0 + (h * ((y0**2) - (y0**3)))
            t += h
            y0 = y1
            x.append(t)
            z.append(y1)
        plt.plot(x, z, label = 'Aproximada')
    
    """
    Função que aproxima o valor de yk de y para a EDO fornecida utilizando o método de Euler implícito.
    """
    def EI(lam, n):
        y0 = 1
        h = 1/n     #h = Tamanho do passo: (1-0)/n
        t = 0
        z =[]       #Lista para os valores de Yk
        x = []      #Lista para os valores de t
        ex = []     #Lista para os valores da solução exata para cada t
        err = []    #Lista para os erros
        x.append(t)
        ex.append(np.exp(-lam*t))
        z.append(y0)
        err.append(abs(ex[0] - z[0]))
        for i in range(1, n):
            y1 = y0/(1+(h*lam))
            y0 = y1
            t += h
            x.append(t)
            z.append(y1)
            ex.append(np.exp(-lam*t))
            err.append(abs(ex[i] - z[i]))
        plt.plot(x, z, label = 'Aproximada')
        plt.plot(x, ex, color = 'r', label='Exata')
        aux = err[0]
        for i in range (1, n):
            if (err[i] > aux): aux = err[i]
        return aux
