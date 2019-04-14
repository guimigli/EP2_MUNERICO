# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:34:56 2019

@author: Tiago e Guilherme
"""

import matplotlib.pyplot as plt
import numpy as np

class ex4:
    
    """
    Método de Euler explícito.
    """
    def EE(delta, n):
        y0 = 1
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