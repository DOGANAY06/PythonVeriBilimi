# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:54:16 2020

@author: Doğan AY
"""


import numpy as np
import pandas as pd

from pandas import Series,DataFrame

ser1 = Series(data=[5,4,6],
              index=["x","m","n"]) 

ser1.sort_index() #en küçüğü al

ser1.sort_values(ascending=False) #büyükten küçüğe sıalama yap 

df = DataFrame(data=np.arange(16).reshape(4,4),
               index=["o","c","t","a"],
               columns=["n","m","j","i"])
df.sort_index(axis=0) #satir indexine göre sırala hangi harf daha önce gelirse onu başa alır 

df.sort_index(axis=1) #sütünları sıralar

df.sort_values(by="m",ascending=False) #m sütununu kücükten büyüğe sırala 

df.sort_values(by="i",ascending=True)