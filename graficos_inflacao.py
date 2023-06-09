# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:12:44 2023

@author: dduca
"""

from bcb import sgs
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 1000)


## Obtendo dados:
ipca = pd.DataFrame(sgs.get({'IPCA': 433}, start='2000-01-01'))
igpm = pd.DataFrame(sgs.get({'IGPM': 189}, start='2000-01-01'))
ippa = pd.DataFrame(sgs.get({'IPPA': 225}, start='2000-01-01'))


## Tratando os dados:
ipca['IPCA'] = (1 + ipca['IPCA'] / 100)
ipca_acum = (ipca.cumprod() - 1) * 100

#igpm.drop(['2023-04-01'], inplace=True)   # iguala a qtd de dados em caso faltante
igpm['IGPM'] = (1 + igpm['IGPM'] / 100)
igpm_acum = (igpm.cumprod() - 1) * 100

#ippa.drop(['2023-04-01'], inplace=True)   # iguala a qtd de dados em caso faltante
ippa['IPPA'] = (1 + ippa['IPPA']/ 100)
ippa_acum = (ippa.cumprod() - 1) * 100

# Gerando o DataFrame
indice = pd.DataFrame([igpm_acum['IGPM'], ipca_acum['IPCA'],
                       ippa_acum['IPPA']]).T

# Plot
fig, img = plt.subplots()
img.plot(indice['IGPM'], label = 'IGPM Acumulado')
img.plot(indice['IPCA'], label = 'IPCA Acumulado')
img.plot(indice['IPPA'], label = 'IPPA Acumulado')
img.set(xlabel='Ano', ylabel='Inflação Acumulada (%)',
        title='Inflação Acumulada desde os anos 2000')
img.grid()
plt.legend()
plt.show()
