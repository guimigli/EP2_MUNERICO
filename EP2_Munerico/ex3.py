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
    def EI(delta, n):
        y0 = delta
        h = 2 / (delta * n)     #h = Tamanho do passo: (2/delta - 0)/n
        t = 0
        z =[]       #Lista para os valores de Yk
        x = []      #Lista para os valores de t
        x.append(t)
        z.append(y0)
        y1 = y0
        for i in range(1, n):
            y1 = ex3.MN(y1, y0, h)
            t += h
            y0 = y1
            x.append(t)
            z.append(y1)
        plt.plot(x, z, label = 'Aproximada')
        
    def F(h, y1, y0):
        return ((h * y1**3) - (h * y1**2) + y1 - y0)
    
    def Flinha(h, y1):
        return ((3 * h * y1**2) - (2 * h * y1) + 1)
        
    def MN(y1, y0, h):
        aux0 = y0
        aux1 = y1
        for i in range (1, 11):
            aux1 = aux0 - (ex3.F(h, aux1, y0) / ex3.Flinha(h, aux1))
            aux0 = aux1
        return aux1
    
fig = plt.figure()
numCol = 15
delta = 0.01
delta2 = 0.0001
limXI = 0
limXF = 200
limYI = -0.01
limYF = 1.02
limYF2 = 0.01
figSize = plt.rcParams["figure.figsize"]
figSize[0] = 6
figSize[1] = 50

#1.3.1
#EE
#n = 120
plt.subplot(numCol,1,1)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EE(delta,120)
plt.title('EE: delta = 0.01 | n=120')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n = 130
plt.subplot(numCol,1,2)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EE(delta,130)
plt.title('EE: delta = 0.01 | n=130')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')     
#n = 140
plt.subplot(numCol,1,3)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EE(delta,140)
plt.title('EE: delta = 0.01 | n=140')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')     
#n = 150
plt.subplot(numCol,1,4)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EE(delta,150)
plt.title('EE: delta = 0.01 | n=150')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')

#EI
#n=30
plt.subplot(numCol,1,5)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EI(delta,30)
plt.title('EI: delta = 0.01 | n=30')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n=40
plt.subplot(numCol,1,6)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EI(delta,40)
plt.title('EI: delta = 0.01 | n=40')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n=50
plt.subplot(numCol,1,7)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EI(delta,50)
plt.title('EI: delta = 0.01 | n=50')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n=60
plt.subplot(numCol,1,8)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EI(delta,60)
plt.title('EI: delta = 0.01 | n=60')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')

#1.3.2
#EE
#n = 120
plt.subplot(numCol,1,9)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF2)
ex3.EE(delta2,10)
plt.title('EE: delta = 0.0001 | n=120')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n = 130
plt.subplot(numCol,1,10)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF2)
ex3.EE(delta2,11)
plt.title('EE: delta = 0.0001 | n=130')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')     

#EI
#n=30
plt.subplot(numCol,1,11)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EI(delta2,30)
plt.title('EI: delta = 0.0001 | n=30')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n=40
plt.subplot(numCol,1,12)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EI(delta2,40)
plt.title('EI: delta = 0.0001 | n=40')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n=50
plt.subplot(numCol,1,13)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex3.EI(delta2,50)
plt.title('EI: delta = 0.0001 | n=50')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n=60
plt.subplot(numCol,1,14)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF2)
ex3.EI(delta2,10000)
plt.title('EI: delta = 0.0001 | n=60')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')