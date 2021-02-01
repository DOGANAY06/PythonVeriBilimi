# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:25:08 2020

@author: Doğan AY
"""

import pandas as pd
plakalar={
      "Tokat":60,
      "Antalya":64,
      "Artvin":15,
      "Corum":19,
      "Ankara":6,
      "Mersin":32,
      "Ankara":6
      } #indexi ve verileri olan bir değişken

data1=pd.Series(plakalar)  #degerleri ve indexi olan değişkeni data serimize yazdırdık

data1.name="Sehirler ve Plakaları"
data1.index.name="Sehirler"


print("Data değerleri()",format(data1.values))

#print("Data özeti \n",data1.describe())

print("Data sehirler()",format(data1.index))

print("Data genel bilgiler:\n",data1.shape,"\n",data1.ndim,"\n",data1.size)

print("Plakaların toplamı=\n",data1.sum())
print("Sehirlerin ortalama plakalası=\n",data1.mean())

print("Minimum degeri:\n",data1.min())
print("Maksimmum degeri:\n",data1.max())

print("İlk bes elemani sehir",data1.head())


print("İlk üc sehir",data1.iloc[:3])
print("Antalyadan ankaraya kadar",data1.loc["Antalya":"Ankara"])

data1=data1.drop_duplicates() #tekrar eden değerleri siler

print(data1)
data1.drop_duplicates(inplace=True) #dasyadan da sil anlamına gelir

data1.drop("Mersin",inplace=True)

print(data1)
