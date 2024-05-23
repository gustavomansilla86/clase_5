def calculadora():
    a= int(input("ingrese primer un numero: "))
    b= int(input("ingrese segundo un numero: "))
    operacion=int(input("ingrese 1 para multiplicar, 2 para dividir, 3 para sumar, 4 para restar: "))
    if operacion ==1:
     resultado=a*b  
     print("el resultado es: ", resultado)

    elif operacion ==2:
     resultado=a/b
     print("el resultado es: ", resultado)
    elif operacion ==3:
     resultado=a+b
     print("el resultado es: ", resultado)
    elif operacion ==4:
      resultado=a-b
      print("el resultado es: ", resultado)


def par():
  lista_n = list(range(20))
  par=[]
  impar=[]
  for n in lista_n:
    if n % 2 == 0:
      par.append(n)
      
    else:
      impar.append(n)
  print("los pares son ",len(par))
  print("lista de pares ",par)
  print( )
  print("los impares son ",len(impar))
  print("lista de impares ",impar)

def entrada():
 
 while True:
  contraseña= str(input("ingrese contraseña: "))
  if contraseña.lower() == "python123":
    print("contraseña correcta")
    break
  else:
    print("contraseña incorrecta")


def primos():
 numero= int(input("ingresar numero: "))
 if numero > 1:
   for i in range(2,numero):
    if numero % i ==0: 
     print("el numero no es primo")
     return
    
    else :
     print("el numero es primo")
    return
 else:
    print("el numero debe ser mayor que 1")

# Genera un número aleatorio entre 1 y 50. Pide al usuario que adivine el número. Utiliza un bucle while para permitir múltiples intentos. Da pistas al usuario si el número ingresado es
# demasiado alto o bajo. Finaliza el juego cuando el usuario adivine correctamente.
def adivinaza():

 numero_aleatorio = 27
 while True:
  intento = int(input("Adivine el número entre 1 y 50: "))
  if intento < numero_aleatorio:
    print("Demasiado bajo, intente de nuevo")
  elif intento > numero_aleatorio:
    print("Demasiado alto, intente de nuevo")
  elif intento == numero_aleatorio:
    print("¡Felicidades! Adivinó el número")
    break


def tablas():
  numero=int(input("ingrese un numero para multiplicar: "))
  for n in range(1,11):
   print(numero,"x ",n,"  = ",numero*n)
tablas()