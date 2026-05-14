#pregunto al usuario por el numero
correcto = False
while correcto == False :
    try:
        numero = int(input("Ingrese un número: "))
        correcto = True
    except ValueError :
        print("Debe ingresar un numero")
#creo mi variable contador
cantidadpares = 0
#recorrer del 1 al numero
for i in range(1,numero+1):
    #verificamos si es par
    if i % 2 == 0:
        print(f"Numero: {i}")
        cantidadpares = cantidadpares + 1

print(f"Cantidad de pares: {cantidadpares}")