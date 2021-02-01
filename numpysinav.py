# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:07:06 2020

@author: Doğan AY
"""

import numpy as np
import numpy.random as rd 

array=np.array([1,2,3])

np.ones((1,5)) #birlik array 1 satir 5 sütündan oluşan 

np.zeros((2,3))

bir=np.ones((2,3))
bir.astype('int')

array=np.arange(10)

array=np.arange(12,26,2)

arraybolme=np.linspace(2,4,8)

diagonal=np.eye(3,3)*4

rastgele=rd.randn(5)

rastgele1=rd.randint(0,10,15).reshape(3,5)


rastgele1=rastgele1**2
array=np.arange(15)
copy_array=array[12:]
copy_array[0]=99

arr_2D=np.arange(25).reshape(5,5)


arr_2D[1:3,2:]  #1 satidan 7 nin olduğu kısım 3 satira kadar al sütünada 2 den başla 






