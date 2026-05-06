edad = int (input("Ingresa tu edad "))
tramo = input ("Ingresa tu tramo de ingresos (A/B/C/D) ").upper()
carga = input ("Tienes carga familiar (si/no) ").upper()

if edad <= 30 and (tramo == "A" or tramo == "B" ) :
    porcentaje = 20
elif edad <= 30 and (tramo == "C" or tramo == "D" ) :
    porcentaje = 10
# hay otra forma elif edad >= 31 and edad <= 60 and tramo == "A" or tramo == "B") :
elif edad <= 60 and (tramo == "A" or tramo == "B") :
    porcentaje = 10
elif edad <= 60 and (tramo == "C" or tramo == "D") :
    porcentaje = 5
else:
    porcentaje = 0

preciobase = 45000
descuento = preciobase * porcentaje / 100
costoplan = preciobase - descuento

#validar si aumento costo por carga familiar

if carga == "si" and (tramo == "A" or tramo == "B" ):
    costocarga = 8000
elif carga == "si" and (tramo == "C" or tramo == "D" ):
    costocarga = 5000
else:
    costocarga = 0

total = costoplan + costocarga

#     SALIDAS
print("**********     PLAN SALUD     **********")
print(f"precio base:                ${preciobase}")
print(f"porcentaje de descuento:    ${porcentaje}")
print(f"costo plan c/descuento:     ${descuento}")
print(f"costo cargas familiares:    ${costocarga}")
print(f"total mensual a pagar       ${total}")

