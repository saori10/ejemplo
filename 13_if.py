# Condicionales
if True:
    print("se ejecuta")

if False:
    print("no se ejecuta")
    

pet = input("¿Cual es tu mascota favorita?")   

if pet == "perro":
   print("genial, tienes buen gusto")
elif pet == "gato":
    print("suerte con el gato")
elif pet == "pez":
    print("me alegro por ti")
else:
    print("no encuentro tu mascota")


stock = int(input("Digita el stock => "))

if stock >= 100 and stock <= 1000:
    print("El stock es correcto")
else:
    print("El stock es incorrecto")


# CREA UN PROGRAMA Q IDENTIFIQUE SI ES NUMERO PAR
number = int(input("Ingrese un numero = "))
result = number %  2
if result == 0:
    print("El numero es par")
else:
    print("El numero es impar") 

