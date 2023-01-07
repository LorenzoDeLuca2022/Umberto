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
