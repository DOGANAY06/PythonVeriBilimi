# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:31:06 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

ser1=Series(np.arange(3),
            index=["A","B","C"])

ser2=Series(np.arange(11,13),
            index=["X","Y"])

pd.concat([ser1,ser2]) #alt alta satir boyunca birleştirme yaptım 

pd.concat([ser1,ser2],axis=1,sort=False) #satir ve sütünları birleştir boş olan değerleri yaz

pd.concat([ser1,ser2],keys=["ser1","ser2"])

pd.concat([ser1,ser2],ignore_index=True) #veri setini birleştir index değelerini yoksay 

df1 =DataFrame(np.random.randn(4,3),
               columns=["X","Y","Z"])

df2 =DataFrame(np.random.randn(3,3),
               columns=["Y","W","X"])

pd.concat([df1,df2],sort=False) #sıralayacak birleştirip

pd.concat([df1,df2],sort=False,keys=["df1","df2"])

pd.concat([df1,df2],sort=True,keys=["df1","df2"]) #alfabetik sırala df1 ve df2 yi birlestir 

pd.concat([df1,df2],sort=True,ignore_index=True)

pd.concat([df1,df2],sort=False,ignore_index=True,join="inner") #hangi sütünlar ortak ona göre birleştir anlamına gelir inner işlemi 

df3 = pd.DataFrame({'W': ['W0', 'W1', 'W2'],
                        'X': ['X0', 'X1', 'X2']},
                         index=['I0', 'I1', 'I2'])
df4 = pd.DataFrame({'Q': ['Q0', 'Q2', 'Q3'],
                    'Y': ['Y0', 'Y2', 'Y3']},
                      index=['I0', 'I2', 'I3']) 


df3.join(df4)

df3.join(df4,how="inner") #ortak olan satırlar alınarak birleştirme işlemi yapılacak 
