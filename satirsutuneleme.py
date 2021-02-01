# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:40:31 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

ser1 =Series(data=np.arange(1,4),
             index=["sat1","sat2","sat3"])

ser1.drop("sat1",inplace=True)  #satir 1 kalici silmek için

ser1.drop(["sat2","sat3"])

df= DataFrame(np.arange(9).reshape(3,3),
              index=["sat1","sat2","sat3"],
              columns=["süt1","süt2","süt3"])

df.drop(labels="süt1",axis=1)

df.drop(columns="süt1")

df.drop(labels="sat2",axis=0)
df.drop(index="sat2")