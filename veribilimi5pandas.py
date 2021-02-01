# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:38:07 2020

@author: Doğan AY
"""


import pandas as pd 

liste_deger=[58,34,6,1]
liste_index=["Sivas","İstanbul","Ankara","Adana"]

data2=pd.Series(liste_deger,index=liste_index) #index ve degerleri veri yani data değişkenimizde tuttuk

print(data2)

plakalar={
      "Tokat":60,
      "Antalya":64,
      "Artvin":15,
      "Corum":19
      } #indexi ve verileri olan bir değişken

data1=pd.Series(plakalar)  #degerleri ve indexi olan değişkeni data serimize yazdırdık

print(data1)


yeni_veri_kümesi=data2.append(pd.Series(data1))  #2 veri setimizi birleştirdik

print(yeni_veri_kümesi) #yeni veri kümemizi ekrana yazdık