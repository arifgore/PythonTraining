#euler34
#Sınır değeri 9!'in 7 katı olarak belirlenmiştir.
import math
toplam = 0
for i in range(10,2540160):
    x = 0
    for t in (str(i)):
        x+=math.factorial(int(t))
    if(x==i):
        toplam+=x
print(toplam) 
