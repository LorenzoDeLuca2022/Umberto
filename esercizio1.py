#Crea un numero casuale tra 10 e 20, mettilo in una variabile z e stampalo

import random
z = (random.randrange(10,20))
print(z)

#Riempi una lista (chiamata listone1) con z numeri casuali tra 0 e 20, dove z è la variabile creata al punto 1.

listone1 = []
for i in range(z):
    listone1.append(random.randrange(0,20))
print(listone1)

#Creare una lista (chiamata listone2) con tutti i numeri della lista listone1 (riempita al punto 2) 
#che sono minori della lunghezza della lista (z)

listone2 = []
for i in (listone1):
    if i < z:
        listone2.append(i)
print(listone2)

#Stampa tutti i valori di listone1 che non sono stati messi in listone2

list3 = []
for i in (listone1):
    if i >= z:
        list3.append(i)
print(list3)

#Eleva al quadrato tutti i valori della lista listone2. (es: 5-> 25)

list4 = []
for i in (listone2):
    list4.append(i**2)
print(list4)

#Fai la somma di tutti i valori di listone2 maggiori di z e stampa il risultato (risultone)

risultone = (0)
for i in (listone2):
    if i > z:
        risultone += i
print(risultone)

#Se risultone sommato alla tua età è maggiore della lunghezza di listone2, stampa 'evviva' Altrimenti stampa 'buuuuu'

if risultone + 22 > len(listone2):
    print("evviva")
else:
    print("buuuuu")