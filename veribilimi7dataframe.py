# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:46:35 2020

@author: Doğan AY
"""

import pandas as pd 

import numpy as np

np.random.seed(24)

df=pd.DataFrame(
        np.random.rand(3,2),
        index=["Ankara","İstanbul","Karaman"],
        columns="Otobüs Kamyon".split() #verileri otobüs ve kamyon sayılarını rastgele atadık
        )

print(df)

plaka={"Ankara":6,"İstanbul":34,"Karaman":70}

nufus={"Ankara":5,"İstanbul":10,"Karaman":1}

araba={"Ankara":56,"İstanbul":145,"Karaman":15}

df2=pd.DataFrame({"plaka":plaka,"nüfus":nufus,"araba":araba}) #veri setimize bazı değişkenler ekleyip tablolaştırdık

print(df2[["plaka"],["taksi"]])