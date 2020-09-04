temp = 0
count = 1
for number in range(1,9999999):
    while(number!=89 and number!=1):
        for i in(str(number)):
            temp += int(i)**2
        number = temp
        temp = 0
    if(number==89):
        count+=1
print(count)



