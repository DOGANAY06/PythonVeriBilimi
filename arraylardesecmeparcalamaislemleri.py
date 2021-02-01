# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:00:18 2020

@author: Doğan AY
"""

import numpy as np

array=np.arange(15)

array[0]

array[-1]

print(array[0:5])


print(array[9:-1:2]) #9 dan başla -1. değere kadar son 2 2 atla

array[0:5]=11 #ilk 5 değeri 11 e çevirir 

array=np.arange(15)

parca_array =array[0:4]

parca_array[:]=11
print(parca_array)

kopya_array =array[0:4].copy() 
print(kopya_array)
array[0:5]=23
print(array)
print(kopya_array)

array_2d =np.array([[0,1,2],[3,4,5],[6,7,8]])
print(array_2d)
array_2d[0]
array_2d[2][1] #array_2d[2,1] aynı değerdir 

array_2d[1:,1:]
array_2d[:2,:2] #2 indexdekiler dahil değil 2 satıra kadar git
array_2d=np.arange(25).reshape(5,5)
array_2d[[0,2]] #0. satır ve 2.satırı al anlamına gelir 
array_2d[:,[1,4]] #ilk kısım bize satırları verir bütün satırlarda 1.ve 4.sütündaki elemanları al anlamındarı 
array[array>10] #arrayde 10 dan büyük değerlerimi yazdır 

