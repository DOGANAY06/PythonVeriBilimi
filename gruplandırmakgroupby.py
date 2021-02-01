# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:33:28 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

df =pd.read_csv("veri_groupby.csv")

grup1 =df.groupby(df["isim"]) #isimleri gruplandir

grup1.groups

grup1.sum() #deger1 ve deger2 ye karşılık gelen yerleri toplar 

grup1.mean() #ortalamasini verir 

grup2 =df["deger1"].groupby(df["renk"])

grup2.max()

df.groupby(["isim","renk"]).groups

df.groupby(["isim","renk"]).sum()

df.groupby("renk").describe().transpose

df.groupby("renk").groups

for renk_adi , grup in df.groupby("renk"):
    print("Bu %s grubudur" % renk_adi) #buradaki %s ifadesi string bir diziyi ekranda göstermek için kullanılır
    print(grup)
    print("\n")
    


