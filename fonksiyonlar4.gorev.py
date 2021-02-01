
def tambolenler(sayi):
    tambolenler=[0]
    for i in range(2,sayi):
        if(sayi%i==0):
            tambolenler.append(i)
    return tambolenler

sayi=int(input("Sayiyi giriniz="))
print(tambolenler(sayi))