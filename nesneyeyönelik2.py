#inheritance (kalıtım) :miras alma

#Person =>name,lastname,age,eat(),run,drink()

#Student(Person),Teacher(Person) classdır aynı özellikleri tekrar oluşturmayacağız

#Animal=> Dog(Animal),Cat(Animal) cat ve dog classdır animaldaki özeliikleri miras alır


class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print("Person kaydedildi")
        
    def who_am_i(self):
        print("Ben bir kisiyim")    
    def eat(self):
        print("Yemek yiyorum ")     
class Student(Person):
        def __init__(self,fname,lname,number):
                Person.__init__(self,fname,lname)
                self.studentnumber=number
                print("Ogrenci kaydedildi")

        
        def who_am_i(self): #override denir buna
                print("Ben bir öğrenciyim")
        def sayHello(self):
                print("Selamünaleyküm ben öğrenciyim")
class Teacher(Person):
        def __init__(self, fname, lname,branch):
                super().__init__(fname,lname)
                self.branch=branch
        def who_am_i(self):
                print(f'Ben bir {self.branch} öğretmeniyim')
            


p1=Person("Dogan","Ay")
p2=Student("Dorukan","Ay",123)
t1=Teacher("Ahmet","Sivri","Din")
t1.who_am_i()
print(p1.firstname+''+p1.lastname)
print(p2.firstname+''+p2.lastname+''+str(p2.studentnumber))
p1.who_am_i()
p2.who_am_i()
p1.eat()
p2.eat()
p2.sayHello()