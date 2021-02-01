# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 12:45:28 2020

@author: Doğan AY
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame

df = pd.read_csv("veri_araba_cross.csv")
#veri okuduk 
df.head() #ilk 5 elemanı yazdirdik 

fig =plt.figure()

axes = fig.add_axes([0,0,1,1])

axes.scatter(df["beygir gücü"],df["agirlik"]) #beygir  gücünün ağırlığa göre grafiği

plt.hist(df["silindir"]) #histogram cubuk grafiki oluşturur

plt.xlabel("silindir sayisi")
plt.ylabel("araba sayisi silindire gore")

plt.boxplot(df["yakit tüketimi"])

df["yakit tüketimi"].describe() #yakit tüketimi açıklası için özellikleri


