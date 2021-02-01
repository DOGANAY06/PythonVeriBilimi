# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:54:15 2020

@author: Doğan AY
"""

import numpy as np
import numpy.random as rd  # rd olarak kısalttık random module çağırıp 

array=rd.randint(1,5,10)

array=array.reshape(5,2)

array+array

array *10
