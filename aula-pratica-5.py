import numpy as np
import scipy.stats
import statistics
import pandas as pd
from math import ceil

#1 Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
#       35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
#   Qual foi a duração média de cada episódio?
minutes = np.array([35, 34, 26, 32, 37, 28, 27, 33, 36, 32])
minutes_pandas = {'Minutos': [35, 34, 26, 32, 37, 28, 27, 33, 36, 32]}
p = pd.DataFrame(minutes_pandas)

average = np.average(minutes)
print(f'1. Média: {average}')

#2 Qual foi a moda?
mode = statistics.mode(minutes)
print(f'2. Moda: {mode}')

#3 Qual foi a mediana?
median = np.median(minutes)
print(f'3. Mediana: {median}')

#4 Por se tratar de um conjunto com poucos dados, calcule a variância amostral.
sample_variance = statistics.variance(minutes)
print(f'4. Variância amostral: {sample_variance}')

#5 Obtenha o desvio padrão por meio do Python.
standard_deviation = p['Minutos'].std()
print(f'5. Desvio padrao: {standard_deviation:.2}')

#6 Em uma caixa de ferramentas, há 4 chaves de fenda e 3 chaves philips.
# Qual é a probabilidade de que uma pessoa, sem olhar para as ferramentas, pegue uma chave de fenda?
tools = 4/7
print(f'6. Probabilidade: {tools:.2} ou {tools * 100:.2f}%')

#7 O tempo médio para a chegada de uma ambulância no local onde precisa prestar
# atendimento tem média de 15 minutos após o chamado com desvio padrão de 3 minutos. Sabendo que os tempos estão de acordo com uma distribuição normal,
# qual é a probabilidade de que uma ambulância chegue entre 10 e 15 minutos?
time = 15
standard_deviation_time = 3
x = 15
y = 10

prob_x = scipy.stats.norm(time, standard_deviation_time).cdf(x)
prob_y = scipy.stats.norm(time, standard_deviation_time).cdf(y)
total = prob_x - prob_y
print(f'7. Total: {total:.2} ou {total * 100:.2f} % ')

#8 Utilizando a fórmula de Slovin, qual é o tamanho da amostra referente a uma
# população de 200.000 dados considerando uma margem de erro de 4%?
N = 200000
e = 0.04
slovin = ceil(N / (1+N*e**2))
print(f'8. Tamanho da amostra: {slovin}')
