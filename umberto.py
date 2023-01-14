#Crea un numero casuale tra 10 e 20, mettilo in una variabile z e stampalo   
import random
z = random.randrange(10,20)
print(z)

#Riempi una lista (chiamata listone1) con z numeri casuali tra 0 e 20, dove z è la variabile creata al punto 1.
lista1 = []
for i in range (z):
    lista1.append(random.randrange(0,20))
print(lista1)
