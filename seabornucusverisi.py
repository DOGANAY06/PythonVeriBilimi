# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 00:24:27 2020

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

#sns.heatmap(data=ucus_data)  #grafla

#fig , ax =plt.subplots(figsize=(10,8))
    
#sns.heatmap(data=ucus_data.loc[:,"1957":],annot=True,ax=axes,
            linecolor="white",linewidth=2)  #annot her bir hücre içindeki gerçek degerleri gösterir 

sns.clustermap(data=ucus_data) #clustermap sınıflama yapıyor 

iris = sns.load_dataset("iris")

iris["species"].unique()  #essiz türleri listeler

sns.pairplot(iris)

iris_grid = sns.PairGrid(iris)

iris_grid.map_diag(sns.distplot)

iris_grid.map_lower(plt.scatter)
iris_grid.map_upper(sns.kdeplot)



