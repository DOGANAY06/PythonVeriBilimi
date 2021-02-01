# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:36:51 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

seri1 =Series(data=np.arange(5,8),
              index=["x","y","z"]) #seri oluşturduk 

seri1["x":"z"]

seri1[seri1>6] #6 dan büyük olanı ver bana

seri1[seri1>6] *=2 #2 ile çarp

df =DataFrame(data=np.arange(20).reshape(5,4),
              index=["x","y","z","m","n"], #satir 
              columns=["A","B","C","D"]) #sütün 

df.loc["z"]
df.iloc[2]

df[(df["B"]>9) | (df["B"]==1)]



