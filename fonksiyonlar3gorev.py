
def asalsayi(a,b):
    for sayi in range (a,b+1): #2.yide işin içine eklemek için +1 dedik a dan başlasın b ye kadar
        for j in range (2,sayi):  #2 den itibaren sayiya kadar böleninin olup olmadığına bakıyoruz
            if (sayi%j==0):
                break
        else:
            print(sayi)


a=int(input("İlk sayiyi giriniz="))
b=int(input("İkinci sayiyi giriniz="))
asalsayi(a,b)
