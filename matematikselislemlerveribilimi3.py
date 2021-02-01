# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:42:20 2020

@author: Doğan AY
"""

import numpy as np

matris=np.array([[1,-3,5],[2,4,6]])

print(np.divide(matris,2))

print(np.sum(matris,axis=1))

print(np.mod(matris,2))

print(np.abs(matris))

print(matris**2) #kare alma işlemi matrislerde 

matris=np.abs(matris) #önce mutlak değerini aldık - li varmı diye 
karekok_matris=np.sqrt(matris) #karekokunu aldık elemanlarin

print(karekok_matris)

print(np.log(matris))

print(np.cos(matris))

print(np.sin(matris))

print(np.tan(matris))

print(np.tan(-1*matris))

