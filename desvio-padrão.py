import pandas as pd

all_weight_cookies_pandas = {'Pesos': [49.7, 50.9, 48.9, 49.8, 50.1, 50.2, 50.8, 49.2, 50.1, 50, 50.4, 48.8, 49.3, 49.5, 49.1, 50.6, 49, 49.7, 49.7, 50.2]}
p = pd.DataFrame(all_weight_cookies_pandas)

desvio_padrao = p['Pesos'].std()
print(f'Desvio padrão: {desvio_padrao}')
