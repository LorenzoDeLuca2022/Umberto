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

#Eleva al quadrato tutti i valori della lista listone2. (es: 5-> 25)
listaQ = []
for n in lista2:
    n=pow(n,2)
    listaQ.append(n)
lista2.clear()
lista2 = listaQ
print(lista2)

#Fai la somma di tutti i valori di listone2 maggiori di z e stampa il risultato (a)
a = (0)
for c in lista2:
    if c > z:
        a = a + c
print(a)

#Se a sommato alla tua età è maggiore della lunghezza di listone2, stampa 'evviva' Altrimenti stampa 'buuuuu'
if (a + 22) > len(lista2):
    print("evviva")
else:
    print("buuuu")
