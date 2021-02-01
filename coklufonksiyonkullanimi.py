# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:16:47 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

pd.read_csv("veri_araba.csv",header=None) #0 dan başla 

df =pd.read_fwf("veri_araba.csv",header=None) #sütün arasındaki boşluk aynıysa bunlar oknması içm 
#data frame cevirdik

df.sum() #3 numaralı sütün string 



df[3].replace('?',0,inplace=True)  # ? soru ,işareti değerlerini 0 ile değiştir kaydet

df[3].dtype # türüne bak 


df.sum()

yeni = ["yakit tüketimi","silindir","yer değiştirme","beygir gücü","agirlik"
        ,"ivmelenme","üretim yili","origin","araba modeli"]

yeni_dict= dict(zip(df.columns,yeni))

df.rename(columns=yeni_dict,inplace=True)

df["yakit tüketimi"].mean() #yakit tüketimi ortalaması için 

df["agirlik"].sum() #toplam ağırlık 

def my_mean(arr): #ortalama hesaplama fonksiyonu 
    return  arr.sum()/len(arr)

def ikiye_bol(arr):
    return arr/2.0

silindir_grup =df.groupby("silindir")
silindir_grup.mean()

silindir_grup.agg(my_mean)

df["ivmelenme"].apply(ikiye_bol)

silindir_grup.describe()

silindir_grup.agg(["max","mean","count"])["yakit tüketimi"]

yakit_grup =df.groupby("yakit tüketimi")
yakit_grup.mean()

yakit_grup.agg(my_mean)

yakit_grup.describe()

yakit_grup.agg(["max","mean","std","count"])["silindir"]

