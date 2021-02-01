mylist=[1,2,3]
myString="My string"

#print(len(myString))
#print(len(mylist))
#print(type(myString))
#print(type(mylist))
class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie objesi oluşturuldu")
    
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("Movie silindi film ")
m=Movie("Filmin adi ","Filmin yazari ",124)

#print(str(mylist))
print(str(m))
#print(len(mylist))
#print(len(m))

#del m
#print(m)