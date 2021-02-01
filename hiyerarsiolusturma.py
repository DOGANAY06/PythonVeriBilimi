# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:08:24 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame
from numpy.random import rand 

ser =Series(data=rand(6),
            index=[[1,1,1,2,2,2],["s1","s2","s3","s1","s2","s3"]])

ser.index
ser[1]["s2"] #1.katman satır2 

df=ser.unstack()

df = DataFrame(np.arange(16).reshape(4,4),
               index=[["a","a","b","b"],[5,6,5,6]],
               columns=[["ank","esk","esk","ist"],["uzak","ykn","uzak","ykn"]])

df.loc["a"].loc[5] #a satırını verir

df.xs(["a",5])

df.index

df.columns

df.index.names=["harf","deger"]
df.columns.names=["sehir","mesafe"]

df.swaplevel("sehir","mesafe",axis=1) #girilen ekseni yer değiştirmeye yarar 

df.sort_index(axis=1,level="mesafe") #büyükten küçüğe sıralama yapıcak 

df.sort_index(axis=0,level="deger") #kücükten büyüge harf sılaması yapıcak

df.xs(6,level="deger")

df.sum(axis=1,level="mesafe") #mesafenin sütünlarındaki değerleri topladı 




