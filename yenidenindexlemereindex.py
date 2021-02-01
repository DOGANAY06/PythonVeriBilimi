# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:36:05 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

list("xyz")

ser1=Series(data=np.arange(1,4),
            index=list("xyz"))
#1 den 4 e kadar olan bir seri yaptık ve listemizi tanımladık 

ser1.reindex(list("xyzm"))
#listede boş bir değer ekledik 
ser1.reindex(list("xyzm"),fill_value=111)

ser2=Series(data=["Ank","Esk","Cor"],
            index=[0,4,19])

ser2.reindex(np.arange(20),method="ffill")

from numpy.random import rand

df =DataFrame(rand(6).reshape(2,3),
              index=["sat1","sat2"],
              columns=["süt1","süt2","süt3"])

df.reindex(labels=["sat1","sat2","sat3"],axis=0)

df.reindex(index=["sat1","sat2","sat3"],method="ffill") #bir önceki satırı yapıyor


df.reindex(index=["sat1","sat2","sat3"],method="bfill") #ilk tanımlanmış halini yapıyor 

df.reindex(index=["sat1","sat2","sat3"],fill_value=1) #boş yer varsa onu 1 ile doldur 

df.reindex(labels=["süt1","süt2","süt3","süt4"],axis=1)

df.reindex(columns=["süt1","süt2","süt3","süt4"])

