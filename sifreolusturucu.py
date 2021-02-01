# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:43:48 2020

@author: Doğan AY
"""

from random import choice

karakter = ["A",1,"B","C","D",2,3,"E","F","Q",7,4,2,3,5,"G","U","I","Z","J",6,8,9,0,"M","N","O","P",
"S","T","K","L","R","T","V","Y","Z"]

print("Sifrenizini uzunluguunu giriniz ?")
sifreuzunluk = int(input())

sifre = ""

for i in range (sifreuzunluk):
    sifre +=str(choice(karakter))
    
print(sifre)