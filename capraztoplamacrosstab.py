# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:08:16 2020

@author: Doğan AY
"""



import pandas as pd

from pandas import DataFrame

df =pd.read_csv("veri_araba_cross.csv")

pd.crosstab(df["silindir"],df["uretim yili"]) #üretim yillarini ve silindir cesidine göre veriyor 

pd.crosstab(df["silindir"],df["uretim yili"],margins=True) #en son silindileri topluyor 
#toplam 398 tane aracım var
pd.crosstab(df["origin"],df["uretim yili"],margins=True)

pd.crosstab(df["origin"],df["uretim yili"],rownames=["yeni_origin"],colnames=["yeni_uretim_yili"])


