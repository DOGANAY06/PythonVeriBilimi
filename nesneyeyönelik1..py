# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:38:43 2020

@author: Doğan AY
"""

#class tanımlama kısmı

class Person:
    #attributes ve methods gerekli içine şimdi onlarıda yapıcaz
    address='no information'
    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("İnit methodu çalisti")
    
    def intro(self): #tanımlanana objenin referansı self instance method selamlama için 
        print("Selamünaleyküm I am "+self.name)
        
    def calculateAge(self):
        return 2020-self.year
#object yani kişi yapıcaz 
p1=Person("Dogan",1990)
p2=Person("Ahmet",1932)

p1.name="serkan"
p1.address="sinop" 
print(f'p1:name:{p1.name} year:{p1.year}address:{p1.address}') #buradaki f format anlamındaki f 
print(f'p2:name:{p2.name} year:{p2.year}address:{p2.address}')
p1.intro() #selamlama için göndereceğimiz attributes
p2.intro()
print(f'yaşım:{p1.calculateAge()} adım:{p1.name}')
print(f'yaşım:{p2.calculateAge()} adım:{p2.name}')

print(p1)
print(p2)
print(p1==p2)

class Circle: #class sefisyesinde tanimlama 
    pi=3.14
    
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
        
    #methods eklicez 
    def cevre_hesapla(self): 
        return 2*self.pi+self.yaricap #cevre hesaplaamak dairede 2 pi * yaricap
    
    def alan_hesapla(self):
        return self.pi *(self.yaricap**2) #dairenin alanı için pi * yaricapin karesi alinir
    
c1=Circle() #otomatik 1 aticak
c2=Circle(5) 

print(f'c1:alan={c1.alan_hesapla()} c1:cevre={c2.cevre_hesapla()}')
print(f'c2:alan={c2.alan_hesapla()} c2:cevre={c2.cevre_hesapla()}')

