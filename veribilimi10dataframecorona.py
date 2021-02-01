# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:03:36 2020

@author: Doğan AY
"""

import pandas as pd

df=pd.read_csv("owid-covid-data.csv",encoding="utf-8")

print(df.count())
print("Boyutum:",df.shape)

df.drop(["new_tests_smoothed","diabetes_prevalence"],axis=1)

print(df.count())

print("Boyut:",df.shape)

print(df.head)

print(df.tail(5))

print(df.dtypes)

kıta=df.drop_duplicates("continent")
print(kıta)

asia=df.groupby(df["continent"]=="Asia")

print(asia.mean())


df.to_csv("düzenleme.csv",encoding="utf-8")