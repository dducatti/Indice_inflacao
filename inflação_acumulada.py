# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:33:49 2023

@author: dduca
"""

from bcb import sgs
import pandas as pd
import matplotlib.pyplot as plt
ipca = {}
igpm = {}
ippa = {}
ipa = {}

def ipca_acum(p=len(ipca), start = '2000-01-01'):
    """    
    Parameters
    ----------
    p : Numero de meses que vai receber a acumulação
        DESCRIPTION. The default is len(ipca).
    start : Inicio da serie historica
        DESCRIPTION. The default is '2000-01-01'.

    Returns
    -------
    f : Retorna o IPCA acumulado para o período
        DESCRIPTION.

    """
    ipca = sgs.get({'IPCA': 433}, start = start)
    ipca['IPCAindex'] = (1 + ipca['IPCA'] / 100)
    acum = pd.DataFrame(ipca[-p:], columns=list(['IPCAindex']))
    acum_produto = acum.cumprod()[-1:]
    f = (acum_produto.iloc[acum_produto.shape[0]-1, 0] - 1) * 100
    return f

    
def igpm_acum(p=len(igpm), start = '2000-01-01'):
    """    
    Parameters
    ----------
    p : Numero de meses que vai receber a acumulação
        DESCRIPTION. The default is len(igpm).
    start : Inicio da serie historica
        DESCRIPTION. The default is '2000-01-01'.

    Returns
    -------
    f : Retorna o IGPM acumulado para o período
        DESCRIPTION.

    """
    igpm = sgs.get({'IGPM': 189}, start = start)
    igpm['IGPMindex'] = (1 + igpm['IGPM'] / 100)
    acum = pd.DataFrame(igpm[-p:], columns=list(['IGPMindex']))
    acum_produto = acum.cumprod()[-1:]
    f = (acum_produto.iloc[acum_produto.shape[0]-1, 0] - 1) * 100
    return f


def ippa_acum(p=len(ippa), start = '2000-01-01'):
    """    
    Parameters
    ----------
    p : Numero de meses que vai receber a acumulação
        DESCRIPTION. The default is len(ippca).
    start : Inicio da serie historica
        DESCRIPTION. The default is '2000-01-01'.

    Returns
    -------
    f : Retorna o IGPM acumulado para o período
        DESCRIPTION.

    """
    ippa = sgs.get({'IPPA': 225}, start = start)
    ippa['IPPAindex'] = (1 + ippa['IPPA'] / 100)
    acum = pd.DataFrame(ippa[-p:], columns=list(['IPPAindex']))
    acum_produto = acum.cumprod()[-1:]
    f = (acum_produto.iloc[acum_produto.shape[0]-1, 0] - 1) * 100
    return f


def ipa_acum(p=len(igpm), start = '2000-01-01'):
    """    
    Parameters
    ----------
    p : Numero de meses que vai receber a acumulação
        DESCRIPTION. The default is len(ipa).
    start : Inicio da serie historica
        DESCRIPTION. The default is '2000-01-01'.

    Returns
    -------
    f : Retorna o IGPM acumulado para o período
        DESCRIPTION.

    """
    ipa = sgs.get({'IPA': 7450}, start = start)
    ipa['IPAindex'] = (1 + ipa['IPA'] / 100)
    acum = pd.DataFrame(ipa[-p:], columns=list(['IPAindex']))
    acum_produto = acum.cumprod()[-1:]
    f = (acum_produto.iloc[acum_produto.shape[0]-1, 0] - 1) * 100
    return f


## Definindo o período em meses
p1 = 12
p2 = 24
p3 = 120

### IPCA
print('-'*40)
a = ipca_acum(p1)
b = ipca_acum(p2)
c = ipca_acum(p3)
d = ipca_acum()
print(f'IPCA Acumulado em {p1}m:\t\t{a:.2f}%')
print(f'IPCA Acumulado em {p2}m:\t\t{b:.2f}%')
print(f'IPCA Acumulado em {p3}m:\t\t{c:.2f}%')
print(f'IPCA Acumulado 01-01-2000:\t{d:.2f}%')
print('-'*40)
### IGPM
e = igpm_acum(12)
f = igpm_acum(24)
g = igpm_acum(120)
h = igpm_acum()
print(f'IGPM Acumulado em {p1}m:\t\t{e:.2f}%')
print(f'IGPM Acumulado em {p2}m:\t\t{f:.2f}%')
print(f'IGPM Acumulado em {p3}m:\t\t{g:.2f}%')
print(f'IGPM Acumulado 01-01-2000:\t{h:.2f}%')
print('-'*40)
## IPP-m :225
i = ippa_acum(12)
j = ippa_acum(24)
k = ippa_acum(120)
l = ippa_acum()
print(f'IPPA Acumulado em {p1}m:\t\t{i:.2f}%')
print(f'IPPA Acumulado em {p2}m:\t\t{j:.2f}%')
print(f'IPPA Acumulado em {p3}m:\t\t{k:.2f}%')
print(f'IPPA Acumulado 01-01-2000:\t{l:.2f}%')
print('-'*40)
#IPA-m :7450
m = ipa_acum(p1)
n = ipa_acum(p2)
o = ipa_acum(p3)
p = ipa_acum()
print(f'IPA Acumulado em {p1}m:\t\t{m:.2f}%')
print(f'IPA Acumulado em {p2}m:\t\t{n:.2f}%')
print(f'IPA Acumulado em {p3}m:\t\t{o:.2f}%')
print(f'IPA Acumulado 01-01-2000:\t{p:.2f}%')























