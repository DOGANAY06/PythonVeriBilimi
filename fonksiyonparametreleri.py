
def add(a,b,c=0):
    return sum((a,b))
def adds(*parametreler):  #bütün göndirilen elemanlar için kullanılır
    return sum((parametreler)) #ne kadar eleman gönderirsen gönder çalışır

def displayUser(**parametreler): #dictionary geleceği için ** yildiz kullandik
    print(type(parametreler))
    for key,value in parametreler.items():
        print("{} is {}".format(key,value))

displayUser(name="Dogan",age=23,city="Istanbul")
displayUser(name="Dorukan",age=11,city="Ankara",phone="213231")
displayUser(name="Hatice",age=42,city="Sivas",phone="42123",email="fdadas@gmail.com")

def myFunct(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)  #a ve b parametreleri dışındaki leri tutar
    print(kwargs)  #değerlerini tutar value 1 ve value 2 gibi
myFunct(10,20,30,40,50,60,70,key1="value 1",key2="value 2")




print(add(21,42))
print(add(24,32,25))

print(adds(24,32,25))
print(adds(32,35,62,72))



def changeName(n):
    n="ada"

name=str(input("İsminizi giriniz="))

changeName(name)
print(name)

def change(n):
    n[0]="istanbul"

sehirler=["Ankara","İzmir"]

change(sehirler[:])

print(sehirler)
