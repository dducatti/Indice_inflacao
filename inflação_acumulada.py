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
    f = ((acum_produto.iloc[acum_produto.shape[0]-1, 0] - 1) * 100).round(2)
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
    f = ((acum_produto.iloc[acum_produto.shape[0]-1, 0] - 1) * 100).round(2)
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
    f = ((acum_produto.iloc[acum_produto.shape[0]-1, 0] - 1) * 100).round(2)
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
    f = ((acum_produto.iloc[acum_produto.shape[0]-1, 0] - 1) * 100).round(2)
    return f


## Definindo o período em meses
p1 = 12
p2 = 24
p3 = 120
p4 = '01/01/2000...'

## IPCA :433
IPCA = [ipca_acum(p1),
        ipca_acum(p2),
        ipca_acum(p3),
        ipca_acum()]

## IGPM :189
IGPM = [igpm_acum(p1),
        igpm_acum(p2),
        igpm_acum(p3),
        igpm_acum()]

## IPP-m :225
IPP = [ippa_acum(p1),
       ippa_acum(p2),
       ippa_acum(p3),
       ippa_acum()]

## IPA-m :7450
IPA = [ipa_acum(p1),
       ipa_acum(p2),
       ipa_acum(p3),
       ipa_acum()]


nomes = ('IPCA %',
         'IGPM %',
         'IPP %',
         'IPA %')

indice = ('Acum.  ' + str(p1) + ' meses',
          'Acum.  ' + str(p2) + ' meses',
          'Acum. ' + str(p3) + ' meses',
          p4)

result = pd.DataFrame(data=(IPCA, IGPM, IPP, IPA),
                      columns=indice,
                      index=nomes).T
print(result)
