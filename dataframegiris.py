# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:22:16 2020

@author: Doğan AY
"""
import numpy as np
import pandas as pd

from pandas import Series,DataFrame

list1=[[0,1,2,3],[4,5,6,7]]

df=DataFrame(data=list1,
             index=['sat1','sat2'],
             columns=['süt1','süt2','süt3','süt4' ])
#2 satir 4 sütündan oluşan bir dataframe tablo oluşturur

df=DataFrame(np.arange(8).reshape(2,4),
              index=['sat1','sat2'],
             columns=['süt1','süt2','süt3','süt4' ])

nba=pd.read_csv('veri_nba.csv') #verilerimizi okumak için yazdık 

type(nba)

nba.head(2) #kaç tane değer istersen onu kullanır 

nba.tail(2) #son kaç tane değeri gözlemlemek için

nba.columns

nba.index

nba['Team']

nba[['Team','Division']]

nba.loc[5]

nba.columns

yeni_sütun=["Siralama","Takim","Galibiyet","Maglubiyet","Oran","İlk Sezon",
            "Toplam Oyun","Bölge"]

dict1 = dict(zip(nba.columns,yeni_sütun)) #yeni sütün değerlerimizi nba daki sütün değerlerine bağla

nba.rename(columns=dict1,inplace=True) #sözlüğü yeniden adlandır listele

nba["Koc"] = np.arange(10) #0 dan 10 a kadar koc sırala 

iki_koc = Series(data=["Dorukan","Dogan"],index =[4,8])

nba["Koc"]=iki_koc

del nba["Koc"]
nba.drop("Takim",axis=1) #takim sütununu herkesten kaldirdik kalici değil ama

