# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 01:13:31 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

df =pd.read_csv("veri_pivot.csv")

df.pivot(index="renk",columns="gün",values="deger") #satir,sütün,değerler gelir 

df.pivot("isim","renk","deger")

df["renk"].unique() #renkte ne çeşit renkler olduğunu bulmak için ulaşıyoruz ,

df["renk"].nunique()

df["isim"].unique()

df["isim"].nunique()
