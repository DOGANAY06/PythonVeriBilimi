# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:24:01 2020

@author: Doğan AY
"""

import pandas as pd
import numpy as np

data={
      "Şubeler":["Ankara","Ankara","İstanbul","İstanbul","İzmir","İzmir","Ankara"],
      "Temsilci":["Ahmet","Mehmet","Dogan","Dorukan","Durmus","Duran","Hatice"],
      "Ciro":[23000,23221,32452,3323,4321,43212,36034]
      }

df=pd.DataFrame(data)
print(df)

subeler=df.groupby("Şubeler")
print(subeler)

print(subeler.min())

print(subeler.max())

print(subeler.mean())

print(subeler.describe())
print(subeler.describe().T)