#dichiaro 2 variabili x e y e le stampo
x = 5
y = "John"
print(x)
print(y)

#dichiaro 2 variabili x una intera una stringa
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#x variabile stringa, y variabile inter, z variabile con decimale
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#tipo di variabile
x = 5
y = "John"
print(type(x))
print(type(y))

#dichiaro che le variabili posso essere scritte sia con virgolette singole che doppie
x = "John"
# is the same as
x = 'John'

#a e A sono due variabili diverse a seconda del caso
a = 4
A = "Sally"
#A will not overwrite a

#diversi nomi per la variabile
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#nomi variabili non validi
#2myvar = "John"
#my-var = "John"
#my var = "John"

#caso cammello, ogni parola tranne la prima comincia con una maiuscola
myVariableName = "John"

#caso Pascal, tutti le parole cominciano con una maiuscola
MyVariableName = "John"

#caso serpente, ogni parola separata da un _
my_variable_name = "John"

#assegnare valori alle variabili su un'unica riga
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#assegnare stesso valore a più variabili
x = y = z = "Orange"
print(x)
print(y)
print(z)

#estrarre valori da una lista e scriverli in variabile
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#uso print () per scrivere variabili
x = "Python is awesome"
print(x)

#uso print () per variabili separate da una virgola
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#posso usare anche +
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#il + per variabili numeriche funziona matematicamente
x = 5
y = 10
print(x + y)

#uso variabile per creare frasi
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#creare una variabile locale
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#variabile globale
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

