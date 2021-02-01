# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:01:13 2020

@author: Doğan AY
"""

def fonk1():
    pass
def fonk():
    print("Merhaba dogan")
    
fonk()

def fonk(isim,renk):
    print("Benim adim {} ve favori rengim {}".format(isim,renk))
    
fonk("Dogan","Pembe")

def toplama(liste):
    toplam=0
    for sayi in liste:
        toplam+=sayi
    return toplam
print(toplama([2,34,32,1]))

def toplama1(*args): #args liste olarak okunuyor 
    toplam=0
    for sayi in args:
        toplam+=sayi
    return toplam
print(toplama1(2,34,32,1))

def isimler_renkler(**kwargs): #dictionary yapısı için kullanılır kwargs
    for isim,renk in kwargs.items():
        print("isim: {} ve favori rengi: {}"
        .format(isim,renk))
isimler_renkler(Dogan="turuncu",Dorukan="pembe",Hatice="mor") 
       
