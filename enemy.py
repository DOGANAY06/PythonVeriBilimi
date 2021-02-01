# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:36:39 2019

@author: Doğan AY
"""
import random
random.random()
class Karakter():
    def __init__(self,can,guc):
        self.can=can
        self.guc=guc
    def vur(self,rakip):
        rakip.can-=self.guc
        x=Karakter.random(1,49)
        y=Karakter(100,16)
        print("Birinci Durum=",x.can)
        y.vur(x)
        print("İkinci durum=",x.can)
        if x.can<=0:
            print("Canavarı geberttin")
        elif x.can>0:
            print("Ücüncü durumda geberttin canavarı",x.can)
            y.vur(x)
        else:
            print("Canavarı gebertemediniz")