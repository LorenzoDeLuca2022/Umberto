#Crea un numero casuale tra 10 e 20, mettilo in una variabile z e stampalo   
import random
z = random.randrange(10,20)
print(z)

#Riempi una lista (chiamata listone1) con z numeri casuali tra 0 e 20, dove z è la variabile creata al punto 1.
lista1 = []
for i in range (z):
    lista1.append(random.randrange(0,20))
print(lista1)

#Creare una lista (chiamata listone2) con tutti i numeri della lista listone1 (riempita al punto 2)
#che sono minori della lunghezza della lista (z)
##Stampa tutti i valori di listone1 che non sono stati messi in listone2
lista2 = []
for x in lista1:
    if x < z:
        lista2.append(x)
    else:
        print(x)
print(lista2)




