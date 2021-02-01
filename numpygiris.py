# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:21:41 2020

@author: Doğan AY
"""

import numpy as np

list1=[0,1,2,3]

array=np.array(list1)

list2=[10,11,12,13]

kom_list =[list1,list2]  #karıştırılmış list

kom_array=np.array(kom_list)

print(kom_array)


sifir =np.zeros((5,2))
print(sifir)

sifir.astype('int')

print(sifir)

np.ones((2,3))
np.empty((5,3))
np.eye(5) #birebirlik matris verir 

np.arange(5)
np.arange(5,10,2) #5 den 10 a kadar yaz ama +2 artırarak 
np.linspace(0,5,11) #kaç tane eş parcaya bölmek istiyorsan başlangıç,bitiş,kac adet 
array=np.arange(10)
