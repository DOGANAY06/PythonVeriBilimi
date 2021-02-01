# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:02:07 2020

@author: Doğan AY
"""

import pandas as pd
import numpy as np
from pandas import DataFrame

import matplotlib.pyplot as plt
import seaborn as sns

bahsis_data =pd.read_csv("veri_bahsis.csv",sep="\t") #veriyi oku  arasına boşluk koy

sns.distplot(bahsis_data["hesap"],kde=True,bins=10,rug=True) #hesabın 5 sütündan ayrılan sütün grafigii görürüz

sns.set_style("darkgrid")

fig,axes = plt.subplots(figsize=(8,2)) #yatayda 8 birim dikeyde 2 birim olacak

sns.distplot(bahsis_data["hesap"],bins=15,rug=True,ax=axes) #hesap grafigimizi 15 parçaya ayırarak oluşturulan tabloya gömdü

sns.jointplot(x="bahsis",y="hesap",data=bahsis_data,kind="kde") #kde nokta grafikyerine gölgelendirme methodu verir

bahsis_data.head()

sns.pairplot(data=bahsis_data,diag_kind="kde",kind="reg",hue="cinsiyet")

sns.barplot(x="gün",y="hesap",data=bahsis_data) #kategorize edilmiş parametreleri bize cizdirir

sns.barplot(x="hesap",y="gün",data=bahsis_data,estimator=np.max)

sns.countplot(x="sigara",data=bahsis_data,hue="cinsiyet")
 
#sigara içen müşteri sayısını veriyor cinsiyete göre dagılımı


sns.boxplot(x ="gün ",y="hesap",data=bahsis_data)  #günlere göre dagilimlar

sns.boxplot(x="zaman",y="hesap",data = bahsis_data,hue="cinsiyet")

sns.violinplot(x="gün",y ="bahsis",data = bahsis_data)

sns.violinplot(x="gün",y="bahsis",data = bahsis_data,hue="cinsiyet",split=True)

sns.stripplot(x="zaman",y="hesap",data = bahsis_data) #noktali grafik

sns.stripplot(x = "hesap",y ="zaman",data = bahsis_data,hue ="sigara")

sns.swarmplot(x="zaman",y="hesap",data = bahsis_data,color="black")
sns.violinplot(x="zaman",y="hesap",data = bahsis_data)

sns.catplot(x ="gün",y="hesap",data=bahsis_data,kind ="bar",hue="sigara") # istedigimiz plotu verdirmek icin
#bar seklinde sigara icenler ve günlük hesap 
sns.catplot(x ="gün",y="hesap",data=bahsis_data,kind ="point",col="sigara")

bahsis_data.head()

bahsis_facet = sns.FacetGrid(bahsis_data,row="sigara",col ="zaman")

#bahsis_facet.map(sns.distplot,"bahsis",ax=axes)

#bahsis_facet.map(plt.hist,"bahsis","hesap")

sns.lmplot(x="hesap",y="bahsis",data=bahsis_data) #lineer regresion bulucak en doğrulugu olan kısmını 

sns.lmplot(x="hesap",y="bahsis",data=bahsis_data,hue="cinsiyet",markers=["o","v"],scatter_kws={"s":150})  #cinsiyete göre hesap ve bahsis
#marker kadınlar o erkekleri V yapar

sns.lmplot(x="hesap",y ="bahsis",data=bahsis_data,row="sigara",col="cinsiyet")
#hesap ve bahsis arasındaki baglantinin sigara ve cinsiyete göre bagı

sns.lmplot(x="hesap",y="bahsis",data=bahsis_data,col="gün",hue="cinsiyet")
#günlerde hesap ve bahsis arasındaki baglantı ve cinsiyet lineer olarak dogrusal 

f = sns.barplot(x="gün",y="hesap",data=bahsis_data)
#isim degistirme islemleri 
f.set_xlabel("hesap günleri")
f.set_ylabel("toplam hesap")

f.set_title("Günlere göre degisim")

f.set(xlabel="",ylabel="",title="")

sns.set_style("ticks")
sns.set_context("talk",font_scale=1.5)
f.set_xlabel("hesap günleri")
f.set_ylabel("toplam hesap")

f.set_title("Günlere göre degisim")

f.set(xlabel="",ylabel="",title="")

sns.despine(left=True,bottom=True)

f =sns.barplot(x="gün",y="hesap")

sns.despine(left=True)

f_figure = f.get_figure()

f_figure.savefig("figure.png",dpi=300)

