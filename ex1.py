# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:58:56 2019

@author: Tiago e Guilherme
"""
import matplotlib.pyplot as plt
import numpy as np

class ex1:
    
    """
    Função que aproxima o valor de yk de y para a EDO fornecida utilizando o método de Euler explícito.
    """
    def EE(lam, n):
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
            y1 = y0*(1-(h*lam))
            t += h
            y0 = y1
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

#1.2
numCol = 14
figSize = plt.rcParams["figure.figsize"]
figSize[0] = 7
figSize[1] = 100
plt.rcParams["figure.figsize"] = figSize
#n = 10
plt.subplot(numCol,1,1)
erroE10 = ex1.EE(100,10)
plt.title('EE: lambda=100 | n=10')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EE: Erro n=10: ", erroE10)
#n = 50
plt.subplot(numCol,1,2)
plt.xlim(-0.01,0.2)
erroE50 = ex1.EE(100,50)
plt.title('EE: lambda=100 | n=50')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EE: Erro n=50: ", erroE50)
#n = 100
plt.subplot(numCol,1,3)
plt.xlim(-0.01,0.2)  
erroE100 = ex1.EE(100,100)
plt.title('EE: lambda=100 | n=100')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EE: Erro n=100: ", erroE100)
#n = 150
plt.subplot(numCol,1,4)
plt.xlim(-0.01,0.2)   
erroE150 = ex1.EE(100,150)
plt.title('EE: lambda=100 | n=150')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EE: Erro n=150: ", erroE150)
#n = 200
plt.subplot(numCol,1,5)
plt.xlim(-0.01,0.2)   
erroE200 = ex1.EE(100,200)
plt.title('EE: lambda=100 | n=200')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EE: Erro n=200: ", erroE200)

#1.3
plt.subplot(numCol,1,6) 
ex1.EE(1000,500)
plt.title('EE: lambda=1000 | n=500')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')

plt.subplot(numCol,1,7) 
ex1.EE(1000,750)
plt.title('EE: lambda=1000 | n=750')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')

plt.subplot(numCol,1,8) 
ex1.EE(1000,1000)
plt.xlim(-0.01,0.025)
plt.title('EE: lambda=1000 | n=1000')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')

plt.subplot(numCol,1,9) 
ex1.EE(1000,1250)
plt.xlim(-0.01,0.025)
plt.title('EE: lambda=1000 | n=1250')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')

#1.4
#n = 10
plt.subplot(numCol,1,10)
erroI10 = ex1.EI(100,10)
plt.title('EI: lambda=100 | n=10')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EI: Erro n=10: ", erroI10)
#n = 50
plt.subplot(numCol,1,11)
plt.xlim(-0.01,0.2)
erroI50 = ex1.EI(100,50)
plt.title('EI: lambda=100 | n=50')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EI: Erro n=50: ", erroI50)
#n = 100
plt.subplot(numCol,1,12)
plt.xlim(-0.01,0.2)  
erroI100 = ex1.EI(100,100)
plt.title('EI: lambda=100 | n=100')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EI: Erro n=100: ", erroI100)
#n = 150
plt.subplot(numCol,1,13)
plt.xlim(-0.01,0.2)   
erroI150 = ex1.EI(100,150)
plt.title('EI: lambda=100 | n=150')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EI: Erro n=150: ", erroI150)
#n = 200
plt.subplot(numCol,1,14)
plt.xlim(-0.01,0.2)   
erroI200 = ex1.EI(100,200)
plt.title('EI: lambda=100 | n=200')
plt.xlabel('t')
plt.ylabel('Y(t)')
plt.legend(loc='upper right')
print("EI: Erro n=200: ", erroI200)


