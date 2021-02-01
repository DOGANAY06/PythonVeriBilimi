# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:21:01 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

ser1 =Series(np.arange(8))

ser1.replace(0,"$",inplace=True) #0 degeri yerine dolar degerini koyduk 

ser1.replace(["$",3],[11,12]) #inplace true olmadığı için bellekte saklanmaz 

ser1.replace({2:55}) #2 değerini 55 ile değiştir 

ser1.replace(4,method="bfill")

ser1.replace(4,method="ffill")

df = pd.DataFrame(np.arange(1,16).reshape(5,3),
                  columns=["A","B","C"])
#1 LE 16 ARASINDA BİR DATAFRAME OLUŞTURDUK

df.replace([1,4,7,10],4)

df.replace([1,4,7,10],[10,7,4,1])

df.replace({"A":1,"B":2},100) #A NIN 1. DEĞERİ B NİN DE BİRİNCİ DEĞERİ DEĞİŞECEK 

df.replace({"C":{3:100,6:100}}) #c deki 3 ve 6 yı 100 ile değiştiricez


