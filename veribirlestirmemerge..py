# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:17:04 2020

@author: Doğan AY
"""

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

df1=DataFrame({"süt1":np.arange(6),"ortak":["a","c","b","c","a","b"]}) #sagdaki dataframe 

df2=DataFrame({"süt2":np.arange(1,4),"ortak":["a","m","b"]}) #soldaki dataframe 

pd.merge(df1,df2)  #ortak sütünlara göre birleştirme işlemi yapar 

pd.merge(df1,df2,on="ortak")

pd.merge(df1,df2,on="ortak",how="left") #ortak elemanları sola koy 

pd.merge(df1,df2,on="ortak",how="right") #sağdakinin kesistiği değerlerin kesisimini gösterir

pd.merge(df1,df2,on="ortak",how="inner") #inner da tanımlamasak olur 

pd.merge(df1,df2,on="ortak",how="outer") #sağ sol dataframe kesisimlerini gösterir 

pd.merge(df1,df2,left_on="süt1",right_on="süt2")

df3 = DataFrame({"ortak1":["Ank","Ank","Esk"],
                 "ortak2":["bir","iki","uc"],
                 "data":[4,5,6]})

df4 = DataFrame({"ortak1":["Ank","Ank","Esk","Esk"],
                 "ortak2":["bir","bir","iki","uc"],
                 "data":[7,8,9,10]})

pd.merge(df3,df4,on=["ortak1","ortak2"],how="outer") #ortak1 deki kelimelere göre eşleştirme yapıyor 

pd.merge(df3,df4,on=["ortak1","ortak2"],how="inner") #ortak noktalarımıza bakar sadece 





