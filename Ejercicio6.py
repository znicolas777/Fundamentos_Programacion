edad = int(input("Ingresa tu edad "))
licencia = (input ("¿tienes licencia? (si/no) "))
licencia = licencia.lower()

if edad >= 18 and licencia == "si":
    print("Puede Conducir")
elif edad >= 18 and licencia == "no":
    print("Debes sacar licencia")
else:
    print("no puedes conducir")
