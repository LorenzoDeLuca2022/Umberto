#Riempi 3 variabili con numeri casuali. Stampa i valori in ordine (dal più piccolo al più grande)
import random
#x = (random.randrange(1,10))
#y = (random.randrange(1,10))
#z = (random.randrange(1,10))
#lista1 = [x,y,z]
#lista1.sort ()
#print(lista1)

#°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸

#Riempi una lista con 5 nomi di automobili e una con 4 Moto, unisci le liste. Stampa la lista risultato in ordine alfabetico
#lista2 = ["Ferrari", "Lamborghini", "Jaguar", "Astor Martin", "McLaren"]
#lista3 = ["Ducati", "Yamaha", "Kawasaki", "Harley-Davidson"]
#lista = lista2 + lista3
#lista.sort ()
#print(lista)

#°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸

#Riempi una lista di 50 numeri casuali. Elimina dalla lista tutti i numeri pari. Stampa la lista
lista4 = []
for i in range (50):
    lista4.append(random.randrange(1,100))
print(lista4)
lista5 = []
for x in lista4:
    if (x % 2) != 0:
        lista5.append(x)
print(lista5)

#°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸

