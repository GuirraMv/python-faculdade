import scipy.stats

media = 5000
desvio_padrao = 300
x = 4700

maior_media = scipy.stats.norm(media, desvio_padrao).cdf(x)-0.5
menor_media = 0.5-scipy.stats.norm(media, desvio_padrao).cdf(x)

probabilidade = maior_media if x > media else menor_media

print(probabilidade)