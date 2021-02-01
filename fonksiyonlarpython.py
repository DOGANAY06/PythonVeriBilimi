def sayHello(name):
    #print("Selamünaleyküm "+name)
    return "SelamünAleyküm " +name
name=str(input("İsminizi giriniz="))
msg=sayHello(name)
print(msg)

def total(num1,num2):
    return num1+num2
num1=int(input("İlk Sayiyi giriniz="))
num2=int(input("İkinci Sayiyi giriniz="))
result=total(num1,num2)
print(result)

def yasHesapla(dogumYili):
    return 2020-dogumYili

dogumYilim=int(input("Dogum yili giriniz"))
age=yasHesapla(dogumYilim)
print(age)

def EmekliligeKacYilKaldi(name,dogumYilim):
    '''
    docstring doğum yılınıza göre emekliliğinize kaç yıl kaldı 

    '''
    age=yasHesapla(dogumYilim)
    emeklilik=65-age
    
    if emeklilik >0:
        print(f'Emekliliğinize {emeklilik} yil kaldi')
    else:
        print("Zeten emekli oldunuz")
    
print(help(EmekliligeKacYilKaldi))
EmekliligeKacYilKaldi(name,dogumYilim)