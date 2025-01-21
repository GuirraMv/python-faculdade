import statistics
import pandas as pd

all_weight_cookies = [49.7, 50.9, 48.9, 49.8, 50.1, 50.2, 50.8, 49.2, 50.1, 50, 50.4, 48.8, 49.3, 49.5, 49.1, 50.6, 49, 49.7, 49.7, 50.2]

# dicionário Python chamado all_weight_cookies_pandas.Ele possui uma única chave chamada "Pesos", que contém uma lista de valores numéricos
all_weight_cookies_pandas = {'Pesos': [49.7, 50.9, 48.9, 49.8, 50.1, 50.2, 50.8, 49.2, 50.1, 50, 50.4, 48.8, 49.3, 49.5, 49.1, 50.6, 49, 49.7, 49.7, 50.2]}

#converte o dicionário para um DataFrame. O DataFrame é uma estrutura bidimensional do Pandas (como uma tabela), onde: As chaves do dicionário se tornam os nomes das colunas. Os valores das listas se tornam as linhas da tabela.
df = pd.DataFrame(all_weight_cookies_pandas)

#MÉDIA
mean = sum(all_weight_cookies)/len(all_weight_cookies)

mean_with_statistics = statistics.mean(all_weight_cookies)

mean_with_pandas = df['Pesos'].mean()

print(f'Média: {mean:.1f}')
print(f'Média (com statistics): {mean_with_statistics:.1f}')
print(f'Méda (com pandas): {mean_with_pandas:.1f}')

#MODA
mode = statistics.mode(all_weight_cookies)
mode_with_pandas = df['Pesos'].mode()

print(f'Moda (com statistics): {mode}')
print(f'Moda (com pandas): {mode_with_pandas}')

#MEDIANA
median = statistics.median(all_weight_cookies)
median_with_pandas = df['Pesos'].median()

print(f'Mediana (com statistics): {median}')
print(f'Mediana (com pandas): {median_with_pandas}')