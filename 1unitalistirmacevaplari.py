# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:05:48 2020

@author: Doğan AY
"""

ulke="Cin"
ulke.capitalize()[:-1]+ulke[-1].capitalize()
print(ulke)
zaman="Aralik"
virus="Corona"

print("{} ülkesinde  {} ayinda {} virusu ortaya cikti".format(ulke,zaman,virus))

lst=[14,2,9,8,12,65,64]

print(lst[1:5])
print(lst[6:])

lst.append(33)
print(lst)
lst.remove(14)
print(lst)

cumle="O zaman baska bir gün bulusalim."

for harf in  cumle:
    print(harf)

for harf in  cumle:
    if harf =='a':
        print("A")
    else:
        print(harf)

def buyukharfli(cumle):
    for harf in  cumle:
        if harf =='a':
            print("A")
        else:
            print(harf)
        
buyukharfli(cumle)