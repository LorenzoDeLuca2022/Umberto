#riempi 3 variabili con numeri casuali. stampa valori dal piu piccolo al piu grande
import random
x = random.random()
y = random.random()
z = random.random()
lista = [x,y,x]
lista.sort()
print (lista)

#riempi una lista con 5 nomi di auto e una con 4 di moto, unisci le liste, stampa la list risultato in ordine alfabetico
list1 = ["McLaren", "Ferrari", "Lamborghini", "Rolls-Royce", "Aston Martin"]
list2 = ["Kawasaki", "Ducati", "Suzuki", "Yamaha"]
list3 = list1 + list2
list3.sort()
print(list3)

#riempi una lista di 50 numeri casuale. elimina numeri pari dalla lista, stampa lista
#list4 = []
#for i in range(50):
#    list4.append(random.randrange(0,50))
#for i in (list4):
#    if (i % 2) == 0:
 #       list4.remove(i)
#print(list4)

#riempi lista con numeri 50 casuali tra 1 e 100 (utlizza ciclo for) e stampa solo numeri > 50 o < 10
list5 = []
list6 = []
for i in range (50):
    list5.append(random.randrange(1,100))
print(list5)
for i in (list5):
    if i > 50 or i < 10:
        list6.append(i)
print(list6)
L = (len(list6))
print(L)