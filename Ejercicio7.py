edad = int(input("Ingresa tu edad "))

if edad >= 18:
    licencia = (input ("¿tienes licencia? (si/no) "))
    if licencia.lower() == "si":
        print("Puede manejar")
    else:
        print("Debe sacar la licencia")
else:
    print("No puedes manejar")