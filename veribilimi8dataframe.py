# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:02:28 2020

@author: Doğan AY
"""

import  pandas as pd

import numpy as np

plaka={"Ankara":6,"İstanbul":34,"Karaman":70}

nufus={"Ankara":5,"İstanbul":10,"Karaman":1}

taksi={"Ankara":56,"İstanbul":145,"Karaman":15}

minibus={"Ankara":46,"İstanbul":100,"Karaman":24}

ucak={"Ankara":6,"İstanbul":45,"Karaman":0}

df2=pd.DataFrame({"plaka":plaka,"nüfus":nufus,"taksi":taksi,"minibus":minibus,"ucak":ucak}) #veri setimize bazı değişkenler ekleyip tablolaştırdık

print(df2)

#print(df2.head(2))

print(df2.tail(2))

print(df2.describe())

print(df2[["plaka","taksi"]]) #köseli parantez içine köseli parantez içinde yazılamlı

df2["Kara tasitlari"]=df2["taksi"]+df2["minibus"]
df2["Hava tasitlari"]=df2["ucak"]
df2.drop("Hava tasitlari",axis=1,inplace=True)
print(df2)
print(df2.loc["Ankara","minibus"]) #istenen değeri çağırmak 
print(df2.loc[["Ankara","İstanbul"],["taksi","minibus"]]) #loc olarak çağırma işlemi yapıyoruz

print(df2[df2>10])
