# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:58:56 2019
@author: Tiago e Guilherme
"""
import matplotlib.pyplot as plt
import numpy as np

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
    
    """
    Função que aproxima o valor de yk de y para a EDO fornecida utilizando o método de Euler implícito.
    """
    def EI(lam, n):
        y0 = 0
        h = (2 * np.pi) / n     #h = Tamanho do passo: (2 * pi - 0)/n
        t = 0
        C = lam / (1 + (lam**2))
        z =[]       #Lista para os valores de Yk
        x = []      #Lista para os valores de t
        ex = []     #Lista para os valores da solução exata para cada t
        # err = []    #Lista para os erros
        exata = C * (np.exp(-lam*t)+ lam * np.sin(t) - np.cos(t)) #Equação para o valor exato
        x.append(t)
        ex.append(exata)
        z.append(y0)
        #err.append(abs(ex[0] - z[0]))
        for i in range(1, n):
            y1 = (y0 + h * lam * np.sin(t + h)) / (1 + h * lam)
            y0 = y1
            t += h
            exata = C * (np.exp(-lam*t)+ lam * np.sin(t) - np.cos(t))
            x.append(t)
            z.append(y1)
            ex.append(exata)
            #err.append(abs(ex[i] - z[i]))
        plt.plot(x, z, label = 'Aproximada')
        plt.plot(x, ex, color = 'r', label='Exata')
        """aux = err[0]
        for i in range (1, n):
            if (err[i] > aux): aux = err[i]
        return aux"""
    
    """
    Função que aproxima o valor de yk de y para a EDO fornecida utilizando o método de Runge-Kutta 4
    """
    def RK44(lam, n):
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
        for i in range(1, n):
            y1 = (y0  + (h * ex2.phi(lam, y0, t, h)))
            y0 = y1
            t += h
            exata = C * (np.exp(-lam*t)+ lam * np.sin(t) - np.cos(t))
            x.append(t)
            z.append(y1)
            ex.append(exata)
        plt.plot(x, z, label = 'Aproximada')
        plt.plot(x, ex, color = 'r', label='Exata')
        
    def func(lam, y, t):
        return lam * (-y + np.sin(t))
        
    def phi(lam, y, t, h):
        return h/6 * (ex2.K1(lam, y, t) + (2 * ex2.K2(lam, y, t, h)) + (2 * ex2.K3(lam, y, t, h)) + ex2.K4(lam, y, t, h))
    
    def K1(lam, y, t):
        return ex2.func(lam, y, t)
    
    def K2(lam, y, t, h):
        return ex2.func(lam, (y + (h/2)*ex2.K1(lam, y, t)), t + h/2)
    
    def K3(lam, y, t, h):
        return ex2.func(lam, (y + (h/2)*ex2.K2(lam, y, t, h)), t + h/2)
    
    def K4(lam, y, t, h):
        return ex2.func(lam, (y + h * ex2.K3(lam, y, t, h)), t + h)

#1.2.1
fig = plt.figure()
numCol = 6
lambd = 10000
limXI = 0
limXF = 8
limYI = -1.01
limYF = 1.01
figSize = plt.rcParams["figure.figsize"]
figSize[0] = 6
figSize[1] = 50
plt.rcParams["figure.figsize"] = figSize
"""#n = 9900
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
ex2.EE(lambd,10050)
plt.title('EE: lambda=10000 | n=10050')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n = 31400
plt.subplot(numCol,1,5)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.EE(lambd,31400)
plt.title('EE: lambda=10000 | n=31400')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n = 31450
plt.subplot(numCol,1,6)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.EE(lambd,31450)
plt.title('EE: lambda=10000 | n=31450')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')"""

#1.2.2
#n=50
plt.subplot(numCol,1,1)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.RK44(lambd,30000)
plt.title('RK44: lambda=10000 | n=50')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')

#1.2.3
#n=50
plt.subplot(numCol,1,2)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.EI(lambd, 50)
plt.title('EI: lambda=10000 | n=50')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
#n=100
plt.subplot(numCol,1,3)
plt.xlim(limXI,limXF)
plt.ylim(limYI,limYF)
ex2.EI(lambd, 100)
plt.title('EI: lambda=10000 | n=100')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')