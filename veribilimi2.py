# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:19:38 2020

@author: Doğan AY
"""

import numpy as np

sifir_matris=np.zeros([2,4])
print(sifir_matris)  #2 satir 4  sütünluk 0 matris

d_sifir_matris=np.zeros((2,4),dtype="int")
print(d_sifir_matris) #integer 0 matris

bir_matris=np.ones((2,4))
print(bir_matris)  #bir matrisi birim matris değildir

d_bir_matris=np.ones((2,4),dtype="int")
print(d_bir_matris)

birim_matris=np.eye(5)
print(birim_matris)

elemanlari_ayni = np.full((2,4),3.14) #2 satir 4 sütünluk 
print(elemanlari_ayni)

rastgele_matris =np.random.rand(4,2) #rastgele sayilardan olusan 4 satirlık 2 sutunluk dizi
print(rastgele_matris)

sifir_bir_arasi=np.empty((2,4))
print(sifir_bir_arasi)

print(bir_matris+elemanlari_ayni)

print(bir_matris-elemanlari_ayni)

print(bir_matris/elemanlari_ayni)

print(np.dot(rastgele_matris,bir_matris)) #çarpma işlemi yapmamızı sağlar 

