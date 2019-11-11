#Ortamdaki kişi sayısına göre herhangi iki kişinin 
#doğum günlerinin aynı olma olasılığını hesaplar.
ks = 1
olas = 1
c = int(input("How many people are there? "))
for ks in range(1, c+1):
    olas = olas * ((365-ks)/365)
print(1-olas)