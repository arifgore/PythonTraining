x = int(input("Kaç kişiyle oynansın? \n"))
liste = list(range(1,x+1,1))
sword = 0
while(len(liste)-liste.count(0) != 1):
    while(sword < x-1):
        liste[sword+1] = 0
        sword += 2
    if(liste[sword-1] == liste[-3]):
        sword = liste.count(0)
    else:
        sword = liste.count(0)-1
    liste.sort()
print(liste[-1])
