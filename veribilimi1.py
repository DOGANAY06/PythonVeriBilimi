# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:27:16 2020

@author: Doğan AY
"""

import numpy as np

dizi=np.array([0,1,3,4,5])

print(type(dizi))

dizi=dizi.astype("float")
print(dizi.dtype)

dizi_2= np.array([[1,3,5,7],[2,4,6,8]])  #satir ve sütünlar için yaptık

print(dizi_2.ndim)  #dizinin boyutunu verir

print(dizi_2.shape) 

d_dizi_2=dizi_2.reshape(1,8)

print(d_dizi_2)

d2_dizi_2=dizi_2.reshape(4,2)

print(d2_dizi_2)

dizi_3=np.arange(0,10)
print(dizi_3)

dizi_3_v1=np.arange(0,10,dtype="float")
print(dizi_3_v1)

dizi_3_v2 =np.arange(0,10,2)  #cift sayiları bastırmak icin

print(dizi_3_v2)
dizi_3_v3=np.arange(1,10,2) #☺tek sayilari bastırmak ici

print(dizi_3_v3)

print(dizi_3_v3[0:])

print(dizi_3_v3[-1]) #son elemanı almak icin

print(dizi_3_v3[0]) #dizinin ilk elemanını bulmak icn


