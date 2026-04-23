clave = input("Ingrese su clave: ")

#Mostramos su longitud total
longitud = len(clave)
print("La logintud de la clave es: ", longitud)
#cantidad minima de longitud
if longitud >= 8:
    print("Longitud OK")
else:
    print("Longitud insuficiente")

#si contiene al menos un numero
if any(c.isdigit() for c in clave):
    print("Contiene números")
else:
    print("No contiene números")
#si es mayusculas, minusculas o mixtos
if clave == clave.upper():
    print("Esta compuesta solo de mayúsculas")
elif clave == clave.lower():
    print("Esta compuesta solo de minúsculas")
else:
    print("Es mixta")
#contraseña sin espacios al principio o final
print("Contraseña: ", clave.strip())