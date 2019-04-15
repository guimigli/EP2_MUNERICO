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
    def EE1(A, n, T, f):
        p = A.shape[0]
        y0 = np.ones((p, 1))
        h = T / n     #h = Tamanho do passo: (2/delta - 0)/n
        x = np.arange(0, T, h)     #Lista para os valores de t
        for step in range(n-1):
            y1 = np.array(y0[:,step] + np.dot(h*A, y0[:,step]) + h*f.T)
            y0 = np.concatenate((y0, y1.T), axis=1)
        for i in range (p):
            plt.plot(x, y0[i])
            
    def EI1(A, n, T, f):
        p = A.shape[0]
        y0 = np.ones((p, 1))
        h = T / n     #h = Tamanho do passo: (2/delta - 0)/n
        x = np.arange(0, T, h)     #Lista para os valores de t
        for step in range(n-1):
            y1 = np.array([np.dot(np.linalg.inv(np.identity(p)-h*A), y0[:,step])])
            y0 = np.concatenate((y0, y1.T), axis=1)
        for i in range (p):
            plt.plot(x, y0[i])
            
    
        

fig = plt.figure()
numCol = 2
limXI = 0
limXF = 200
limYI = -0.01
limYF = 1.02
limYF2 = 0.01
figSize = plt.rcParams["figure.figsize"]
figSize[0] = 6
figSize[1] = 6          
#2.1.1

A11 = np.array([[-2, 0, 0, 0, 0],
            [0, -4, 0, 0, 0],
            [0, 0, -6, 0, 0],
            [0, 0, 0, -8, 0],
            [0, 0, 0, 0, -10]])
    
f1 = np.array([[0],
               [0],
               [0],
               [0],
               [0]])
    
T = 5
#EE
#n = 100
plt.subplot(numCol,1,1)
#plt.xlim(limXI,limXF)
#plt.ylim(limYI,limYF)
ex4.EE1(A1, 100, T, f1)
plt.title('EE: n=150')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n = 100
plt.subplot(numCol,1,2)
#plt.xlim(limXI,limXF)
#plt.ylim(limYI,limYF)
ex4.EI1(A1, 100, T, f1)
plt.title('EI: n=150')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')





