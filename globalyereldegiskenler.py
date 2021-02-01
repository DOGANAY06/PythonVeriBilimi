
#x="global x"

#ef function():
    #x="local x"
    #print(x)

#function()
#print(x)

name="Dogan" #global olarak tanımlanan name deyimi

def changeName(new_name): #fonksiyonda tanımlı local name değeri
    name=new_name
    print(name)
changeName("Dorukan")
print(name)


name="global string"

def greeting():
    name="Doganim"

    def hello():
        print("Selamünaleyküm "+name)
    
    
    hello()
greeting()

x=50
def test():
    global x
    print(f"x : {x}") #bizim global ilk x değişkenimiz
    x=100
    print(f"Değiştir x to {x}")

test()
print(x)








