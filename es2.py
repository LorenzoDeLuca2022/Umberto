#Crea un numero casuale tra 10 e 30, mettilo in una variabile n e stampalo
import random
n = random.randrange(10,30)
print(n)

#Riempi una lista list1 con n numeri casuali tra 0 e 30, dove n è la variabile creata al punto 1.
list1 = []
for x in range(n):
    list1.append(random.randrange(0,30))
print(list1)


#Stampa tutti i numeri della lista list1 (riempita al punto 2) che sono maggiori della lunghezza della lista
list2 = []
for x in list1:
    if x > (len(list1)):
        list2.append(x)
print(list2)

#Riempi una nuova lista list3 con i valori  che non sono stati stampati al punto 3
list3 = []
for x in list1:
    if x < (len(list1)):
        list3.append(x)
print(list3)

#Rendi negativi tutti i valori della lista list3 . (es: 5-> -5) e stampa la lista
list4 = []
for x in list3:
    x = -x
    list4.append(x)
list3.clear()
list3.extend(list4)
print(list3)

#Fai la somma di tutti i valori di list3 (dopo averli resi negativi al punto 5) e stampa il risultato (ris)
ris = (0)
for x in list3:
    ris = ris + x
print(ris)

#Calcola il valore assoluto di ris. Se ris è maggiore della lunghezza di list3 , stampa 'evviva' Altrimenti stampa 'buuuuu'
ris = abs(ris)
if ris > (len(list3)):
    print("evviva")
else:
    print("buuuu")

    
