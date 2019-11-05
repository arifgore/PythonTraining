#asalmı
import math
def asal():
    bol = 3
    p = math.floor(sayi**(1/2))
    if(sayi == 2):
        return(1)
    elif(sayi/2 == math.floor(sayi/2)):
        return(0)
    while(bol < p+1):
        if(sayi/bol == math.floor(sayi/bol)):
            return(0)
        bol+=2        
    return(1)
sayi = 1
while(sayi != 0):
    sayi = int(input("sayıyı giriniz... ")) 
    if(asal() == 1):
        print(sayi, " sayısı asal sayıdır. ")
    else:
        print(sayi, " sayısı asal değildir. ")    