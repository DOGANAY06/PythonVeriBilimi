
def square(num):
    return num**2

numbers=[1,3,5,9,10,4]
#map(square,numbers) #map metodu ile kullanılacak dizi verilir ve bütün elemanları kullanılır

result1=list(map(square,numbers))
result2=list(map(lambda num:num**2,numbers)) #square meethodunun yaptığı işlemi yaparız
result=square(2)
print(result)
print(result1)
print(result2)

def check_even(num):
    return num%2==0
result3=list(filter(check_even,numbers))
result4=list(filter(lambda num:num%2>0,numbers))
print(result3)
print(result4)