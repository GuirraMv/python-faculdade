from math import ceil

N = 20000
e = 0.02

# fórmula de Slovin
n = ceil(N / (1+N*e**2))

print(f'Tamanho da amostra: {n}')