# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:57:08 2020

@author: Doğan AY
"""

import pandas as pd
import numpy as np
from pandas import DataFrame

import matplotlib.pyplot as plt
import seaborn as sns

ucus =pd.read_csv("veri_ucus.csv")

ucus.head

ucus_data = ucus.pivot(index="ay",columns="yil",values="yolcu_sayisi")
sns.clustermap(data=ucus_data) #clustermap sınıflama yapıyor 