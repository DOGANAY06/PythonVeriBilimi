# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:01:43 2020

@author: Doğan AY
"""

import numpy as np

matris=np.arange(0,50)

matris=matris.reshape((10,5))

print(matris)

print(matris[matris>=5])
print(matris[matris<5])

print(matris[matris==5])

print(matris[(matris<5)& (matris>2)])

print(matris[(matris<10) | (matris<4)])

print(matris[matris%2==0])