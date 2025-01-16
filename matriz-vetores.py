import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import pandas as pd
from scipy.interpolate import *

# preco_venda = np.array([[22, 12, 54, 89, 11]])
# preco_custo = np.array([[18,4,39,61,8]])
# contribuicao = preco_venda - preco_custo
# print(contribuicao)

# preco_venda = np.array([[22, 12, 54, 89, 11]])
# preco_frete = np.array([[3,2,1,4,1]])
# total = preco_venda + preco_frete
# print(total)

# notas = np.array([[90,85,70,100]])
# pesos = np.array([[0.2,0.2,0.3,0.3]])
# notal_final = np.inner(notas,pesos) #obtendo produto escalar
# print(notal_final)

# array = np.array([[3,2,-1], [5,0,20]])
# print(array)


# vetor = [22, 12, 54, 89, 11]
# # array = np.array(vetor)
# real = list(map(lambda dolar: dolar * 6, vetor))
# print(real)

# vetor = [138.40, 86.70, 90.90, 234.90, 107.70]
# array = np.array(vetor)
# real = list(map(lambda dolar: dolar * 5.10, vetor))
# print(real)

# matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# teste = matriz * 2
# matriz = np.array([[22, 12, 54, 89, 11]])
# print(teste)

# v=np.array([[22, 12, 54, 89, 11]])
# u=np.array([[18, 4, 39, 61, 8]])
# m=v-u
# print(m)

# v=np.array([[3,6,-1]])
# u=np.array([[11,14,9]])
# w=v+u
# print(w)

# u=np.array([[3,6,-1]])
# v=np.array([[11,14,9]])
# w=u*v
# print(w)

# u=np.array([[134.10, 112.87, 146.02, 151.19, 147.08, 136.32]])
# v=np.array([[89.10, 78.50, 94.09, 101.44, 89.99, 90.04]])
# media=u+v
# print(media)

# x=np.linspace(0, 10, 100)
# y=28*x
# plt.plot(x,y)
# plt.show()

# a=-340
# b=5700
# c=-9500
# delta=b**2-4*a*c
# yv=-delta/(4*a)
# print(yv)

# N=20000
# e=0.02
# n=N/(1+N*e**2)
# print(f'Tamanho da amostra: {n}')

# N=150000
# e=0.03
# n=ceil(N/(1+N*e**2))
# print(f'Tamanho da amostra: {n}')

# x=[0, 5, 8]
# y=[6, 2,15]
# p=lagrange(x, y)
# print(p)

# x=np.linspace(0, 16, 100)
# y=-340*x**2+5700*x-9500
# plt.plot(x,y)
#
# a=-340
# b=5700
# xv=-b/(2*a)
# print(xv)
#
# a=0
# b=28
# c=-10
# xv=-b/(2*a)
# print(xv)
#
# delta=b**2-4*a*c
# yv=-delta/(4*a)
# print(yv)