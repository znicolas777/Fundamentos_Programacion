nombre = input ("Ingrese el nombre de la mascota ")
especie = input ("Que tipo de mascota es (perro/gato) ")
peso = float (input("Ingrese el peso de la mascota "))

if especie == "perro":
    if peso < 10:
        print("nombre de mascota: ", nombre)
        print("Cantidad de letras:", len(nombre))
        print("Consulta pequeña- $15.000")
    else:
        print("Nombre de mascota: ",nombre)
        print("Cantidad de letras: ", len(nombre))
        print("Consulta grande- $22.000")
elif especie == "gato":
    print("Nombre mascota: ",nombre)
    print("Cantidad de letras: ", len(nombre))
    print("Consulta grande -22.000")
else:
    print("Especie no atendida en esta clinica")

