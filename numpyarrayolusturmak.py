# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:45:48 2020

@author: Doğan AY
"""

import numpy as np
import numpy.random as rd  # rd olarak kısalttık random module çağırıp 

rd.rand(10) #rastgele 10 tane sayı
rd.randint(2,5,10) #2 den 5 e kadar rastgele 10 tane sayı oluştur anlamında 

array=rd.randint(2,5,10)

array.reshape(5,2) #yeniden sekillendirme 
