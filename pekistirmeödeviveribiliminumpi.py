# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:15:01 2020

@author: Doğan AY
"""

#1 den 100 e kadar 10 10 matris oluşturma

import numpy as np

matris=np.arange(0,100)

matris=matris.reshape((10,10))

print(matris)

print(matris[matris<20])

print(matris[matris>60])

print(np.any(matris<0))

print(np.all(matris>0))

print(matris[matris%3==0])
#matris=np.divide(matris,3)

print(matris[matris%3!=0])