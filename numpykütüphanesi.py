# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:51:29 2020

@author: Doğan AY
"""

import numpy as np

from scipy import stats

matris=np.arange(0,10,dtype="int")
print(matris)
print(np.min(matris))

print(np.max(matris))

print(np.mean(matris)) #ortanca deger

matris2=np.eye(5)

print(matris2)

print(stats.mode(matris2)) #frekansı bulmak için

print(np.std(matris2)) #standart sapma

print(np.var(matris2)) #varyans