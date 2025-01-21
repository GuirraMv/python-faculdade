import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import pandas as pd
from scipy.interpolate import *


# 1. Utilize o Python para gerar um conjunto de números inteiros que variam de -10 a
# 20. Em seguida, verifique se o número -1 está neste conjunto.

#Resposta
numbers = np.arange(-10, 20)
has_number = -1
print(f'Questão 1: {numbers.__contains__(has_number)}')

# 2. Verifique se o número -11 está neste conjunto.

#Resposta
has_number = -11
print(f'Questão 2: {numbers.__contains__(has_number)}')

# 3. No conjunto a seguir são apresentados os valores dos salários mínimos de 1995
# a 2022 dispostos em ordem cronológica.
# S={100, 112, 120, 130, 136, 151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510,
# 540, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1039, 1045, 1100, 1212}
# Verifique, por meio do Python, se o valor R$ 350,00 está neste conjunto.

#Resposta
minimal_wage = {100, 112, 120, 130, 136, 151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510,
 540, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1039, 1045, 1100, 1212}
has_value = 350
print(f'Questão 3: {minimal_wage.__contains__(has_value)}')

# 4. Para a entrada em uma residência, foram criadas 5 senhas numéricas: 452012,
# 323233, 787910, 528917 e 683524. Por meio do Python, crie um programa que
# armazena estas senhas em um conjunto e verifica se a senha digitada pelo usuário
# está ou não neste conjunto para permitir ou proibir a entrada na residência.

#Resposta
# passwords = [452012, 323233, 787910, 528917, 683524]
# input_password = int(input("Questão 4: Digite a senha: "))
# correct_password = input_password in passwords
# validate_password = "Senha correta" if correct_password == True else "Senha incorreta"
# print(validate_password)

# 5. O vetor v contém os preços de venda de algumas mercadorias:
# v=(1210, 897, 1230, 1495, 799, 890, 1010)
# A loja está com uma promoção onde é dado um desconto de 20% em todas as
# mercadorias. Por meio do Python, obtenha o vetor que contém os preços destas
# mercadorias com o desconto.

#Resposta
original_value=np.array([[1210, 897, 1230, 1495, 799, 890, 1010]])
discount_value= original_value - (original_value * 20) / 100
print(f'Questão 5: {discount_value}')


# 6. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u+v utilizando o
# Python.

#Resposta
u = np.array([[3,4,8]])
v = np.array([[10,12,-1]])
sum = u+v
print(f'Questão 6: {sum}')

# 7. obtenha o vetor u-v utilizando o Python.

#Resposta
subtraction = u-v
print(f'Questão 7: {subtraction}')

# 8. obtenha o vetor u.v utilizando o Python.

#Resposta
multi = u*v
print(f'Questão 8: {multi}')

#9. Considere as matrizes
# A = [3,5,9
#      4,3,2
#      1,5,-5]

# B = [12,-6,7
#      3,0,2
#      -1,10,1]

#Utilize o Python para obter a matriz C=A+B.

#Resposta
array_a = np.array([[3,5,9], [4,3,2], [1,5,-5]])
array_b = np.array([[12,-6,7], [3,0,2], [-1,10,1]])
array_c = array_a+array_b
print(f'Questão 9: {array_c}')

#10. Utilize o Python para obter a matriz C=A*B.

#Resposta
array_c_multi = array_a*array_b
print(f'Questão 10: {array_c_multi}')

#11. Construa o gráfico da função y=x**3-2x**2+12x-1 no intervalo [-3, 4].

#12. Quais são as coordenadas do vértice da função f(x)=-2x**2+21x-8?



#13. Uma empresa produz carregadores para um determinado modelo de telefone
# celular e precisa obter a função que relaciona o lucro mensal com o preço de venda
# dos carregadores. Os custos fixos mensais da empresa correspondem a R$
# 47.500,00. Para um preço de venda de R$ 12,00 por unidade, o lucro mensal
# corresponde a R$ 22.000,00. Quando cada carregador é vendido por R$ 20,00, o
# lucro mensal é de R$ 20.450,00. Obtenha o polinômio interpolador que relaciona o
# lucro y com o preço de venda x.

#14. Obtenha a soma 7+8 módulo 12.

#Resposta
mod = (7+8)%12
print(f'Questão 14: {mod}')