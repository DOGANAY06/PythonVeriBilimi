# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:08:32 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series

liste_1=[3.0,2.5,3.25,3.8]
liste_1

ortalama=Series(data=liste_1,index=['A','B','C','D'])

array =np.array(liste_1)

ortalama=Series(data=array,index=['A','B','C','D'])

sozluk_1 = {'A':3.0,'B':2.5,'C':3.25,'D':3.8}

ortalama=Series(sozluk_1)

ortalama >3.0
'A' in ortalama

ortalama.values
ortalama.index

isimler=['Berk','Melih','Dogan','Dorukan']
ortalama=Series(data=ortalama.values,index=isimler,
                name='1.dönem ortalamasi')
ortalama.index.name='Ogrenciler'
ortalama_2=Series(data=[1.8,2.0,0.9,3.0],index=isimler,
                  name='2.dönem ortalamasi')
(ortalama+ortalama_2) /2 #ogrencilerin 1.dönem ve 2.dönem not ortalamasi

ortalama_2=Series(data=[1.8,2.0,0.9,3.0],index=isimler,
                  name='2.dönem ortalamasi')

