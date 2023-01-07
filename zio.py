#crea un numero casuale tra 10 e 30. mettilo in una variabile n e stampalo
import random
n = (random.randrange(10,30))
print(n)

#riempi una lista list1 con n numeri casuali tra 0 e 30 dove n è la variabile al punto 1
list1 = []
for i in range(n):
    list1.append(random.randrange(0,30))
print(list1)

#stampa tutti i numeri della list1 che sono maggiori della lunghezza della lista
list2 = []
for i in (list1):
    if i > len(list1):
        list2.append(i)
print(list2)

#riempi una list3 con i valori che non sono stati stampati al punto 3
list3 = []
for i in (list1):
    if i <= len(list1):
        list3.append(i)
print(list3)

#rendi negativi tutti i valori della list3 e stampa lista
for i in range(len(list3)):
    list3[i] = -list3[i]
print(list3)

#stesso esercizio di sopra ma eleva al quadrato i valori della list3
#for i in range(len(list3)):
#    list3[i] = list3[i]**2
#print(list3)

#fai la somma di tutti i valori di list3 dopo averli resi negativi al punto 5 e stampa il risultato ris
ris = 0
for i in (list3):
    ris += i
print(ris) 

#calcola il valore assoluto di ris, se ris è maggiore lunghezza list3 stampa evviva altrimenti stampa buuu
if abs(ris) > len(list3):
    print("evviva")
else:
    print("buuu")