"""enumerate
marcas = ["Toyota", "Ford", "Honda", "Chevrolet", "Nissan", "Hyundai", "Subaru", "Volkswagen", "Mercedes-Benz", "BMW"]
print(marcas)
for indice,marcas in enumerate(marcas):
    print(indice,marcas)"""

"""RANGE
rango= range(1,6)
numeros= list(rango)
print (numeros)"""

"""ZIP
nombre= ("gustavo","gabriel","mansilla")
edad=(37,38,39)
personas= zip(nombre,edad)
print(list(personas))"""


"""asignaciones
a=b=c=5
print("valor de a= ",a,"valor de b= ",b,"valor de c= ",c)
a,b,c=[1,2,3]
print("valor de a= ",a,"valor de b= ",b,"valor de c= ",c)"""

"""
"desenpaquetado con *"
lista= [1,2,3,4,5]
a,*b,c = lista
print("valor de a= ",a,"valor de b= ",b,"valor de c= ",c)"""

""" interadores 
numero = int(input("ingrese un numero: "))
if numero > 0:
    print("el numero es positivo")
elif numero < 0 :
    print("el numero es negativo")
else :
    print("el numero es cero")"""

"""edad= int(input("ingrese su edad: "))
persona= "menor" if edad < 18 else "mayor"
"""


def mayor():
  a=int(input("ingrese un numero: "))
  b=int(input("ingrese otro numero: "))
  if a > b :
    print("Hola Politecnico Malvinas")
def diferencia():
  a=int(input("ingrese un numero: "))
  b=int(input("ingrese otro numero: "))
  
  if a != b:
   print("Hola Politecnico Malvinas")    
def distinto_o_iguales():
 a=int(input("ingrese un numero: "))
 b=int(input("ingrese otro numero: "))
 if a == b :
   print("son iguales")
 else: 
  print("son distintos")
def imprimir():
  a=int(input("ingrese un numero: "))
  b=int(input("ingrese otro numero: "))
  if a == b:
    print("imprimir 1")
  elif a > b:
    print("imprimir 2")
  else:
    print("imprimir 3")

def igualdades_dobles():
  a=int(input("ingrese un numero: "))
  b=int(input("ingrese otro numero: "))
  c=int(input("ingrese otro numero: "))
  d=int(input("ingrese otro numero: "))
  if a == b and c == d :
    print("Hola Politecnico Malvinas")

def iguadad():
   a=int(input("ingrese un numero: "))
   b=int(input("ingrese otro numero: "))
   c=int(input("ingrese otro numero: "))
   d=int(input("ingrese otro numero: "))
   if a==b or c==d:
     print("Hola Politecnico Malvinas")

def edad():
  edad=int(input("ingrese su edad: "))
  if edad < 18 :
    print("menor de edad")
  else:
    print("mayor de edad")

def par_o_impar():
   a=int(input("ingrese un numero: "))
   if a % 2 == 0:
     print("es par")
   else :
     print("es impar")
def maximo():
     a=str(input("ingrese un numero separados por una coma: "))
     b=a.split(",")
     numero= max(b)
     print(numero)
def bienvenido():
  nombre=str(input("ingrese su nombre: "))
  if len(nombre)>1:
    print("Bienvenido " + nombre)
  else:
    print("Bienvenido anonimo")

def bloque_while() :
  a = 0
  while a < 5:
    print("numero: ",(a))
    a += 1



def bandera():
  bandera = True 
  while bandera :
      nombre = input("por favor ingrese nombre: ")
      if len(nombre) ==0 :
        print("no a ingresado nombre")
      else:
        print(f"bienvenido "+ nombre)
        bandera = False


def bucle_for(): 
    for i in range(26):
      if i > 2 and i % 1 == 0:
        print("numero: ",(i))


# lista=list(range(0,10,2)) inicio, final , saltos y si se quiere se puede hacer en negativo con saltos -2
# print(lista)

def break_prueba():
  for i in range(10):
    if i == 10:
      break
    print(i)

def continue_pruba():
  nombres =["juan","gustavo","gabriel","natalia","luz","carolina"]
  for nombre in nombres :
    if len(nombre) == 3:
      continue 
    print(nombre)


def bucles_intinerantes():
  numeros= range(21)
  for num in numeros :
    print(num)


def while_20():
  numeros= 0
  while numeros > 20:
   print(numeros)
   numeros += 1
while_20()