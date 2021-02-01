# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:33:50 2020

@author: Doğan AY
"""

import numpy as np
import numpy.random as rd 

array=np.arange(15).reshape(5,3)

array.sum()#bütün sayilarin toplami icin 

array.sum(axis=0) #satir boyunca 0.satırdan başla asağı dogru 

array.sum(axis=1) #sütün boyunca topla 

array.max(axis=0) #en yüksek değerli satırı bul 

array.max(axis=1) 

array.argmax(axis=0)

array.min(axis=0) #hangi satirdaki değer en kücükse onu verir

array.var() #varyans değerini verir

array.std() #standart sapma değerini verir 

array.mean(axis=0) #satirlarin ortalamasini verir 

array.mean(axis=1) #sütünların ortalamasını verir 

siralama_array=rd.randn(12).reshape(4,3)

siralama_array.sort(axis=1) #kücükten büyüge sutun sıralama 

siralama_array.sort(axis=0) #kücükten büyüge satir siralam 

sehir=np.array(["Ankara","Adana","Sivas","Karaman","Konya"])
sehir.sort()
np.unique(sehir) #her şehri tek defa tekrarlar 
np.in1d("Karaman",sehir) #aranan şey var mı yok mu true olarak gsterir 

array.shape[0] #arrayin kaç satirli olduğunu bulur

array.shape[1]  #arrayin kaç sütünlu olduğunu bulur

array.size  #toplam kaç tane eleman olduğunu bulur 

mantik=np.array([True,False,True,False])

mantik.any() #herhangi bir doğru değer 
mantik.all() #yanlis deger varsaa onu gösterir 



