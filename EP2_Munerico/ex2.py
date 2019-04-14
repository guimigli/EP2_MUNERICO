# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:58:56 2019
@author: Tiago e Guilherme
"""
import matplotlib.pyplot as plt
import numpy as np
from decimal import *

class ex2:
    
    """
    Função que aproxima o valor de yk de y para a EDO fornecida utilizando o método de Euler explícito.
    """
    def EE(lam, n):
        y0 = 0
        h = (2 * np.pi) / n     #h = Tamanho do passo: (2 * pi - 0)/n
        t = 0
        C = lam / (1 + (lam**2))
        z =[]       #Lista para os valores de Yk
        x = []      #Lista para os valores de t
        ex = []     #Lista para os valores da solução exata para cada t
        #err = []    #Lista para os erros
        exata = C * (np.exp(-lam*t)+ lam * np.sin(t) - np.cos(t)) #Equação para o valor exato
        x.append(t)
        ex.append(exata)
        z.append(y0)
        #err.append(abs(ex[0] - z[0]))
        for i in range(1, n):
            y1 = (y0 * (1 - (h * lam))) + (h * lam * np.sin(t))
            y0 = y1
            t += h
            exata = C * (np.exp(-lam*t)+ lam * np.sin(t) - np.cos(t))
            x.append(t)
            ex.append(exata)
            z.append(y1)
            #err.append(abs(ex[i] - z[i]))
        plt.plot(x, z, label = 'Aproximada')
        plt.plot(x, ex, color = 'r', label='Exata')
        """aux = err[0]
        for i in range (1, n):
            if (err[i] > aux): aux = err[i]
        return aux"""
    
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

#1.2.1
fig = plt.figure()
numCol = 5
lambd = 10
limXI = 0
limXF = 8
limYI = -1.01
limYF = 1.01
figSize = plt.rcParams["figure.figsize"]
figSize[0] = 7
figSize[1] = 60
plt.rcParams["figure.figsize"] = figSize
#n = 9900
plt.subplot(numCol,1,1)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.EE(lambd,9900)
plt.title('EE: lambda=10000 | n=9900')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n = 9950
plt.subplot(numCol,1,2)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.EE(lambd,9950)
plt.title('EE: lambda=10000 | n=9950')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n = 10000
plt.subplot(numCol,1,3)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.EE(lambd,10000)
plt.title('EE: lambda=10000 | n=10000')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n = 10050
plt.subplot(numCol,1,4)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.EE(lambd,50)
plt.title('EE: lambda=10000 | n=10050')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')