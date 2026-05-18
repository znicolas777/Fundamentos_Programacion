cantidad = 0
placa = ""
capacidad = 0
pesados = 0
ligeros = 0

while cantidad <= 0:
    try:
        cantidad = int(input("Ingrese cuantos vehiculos desea registrar: "))
        if cantidad  <= 0:
            raise ValueError
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar")
for z in range(1,cantidad + 1):  
    cumple = False   
    while not cumple:
        placa = input("Ingresa la patente del vehiculo: ").upper()
        if len(placa) >= 6 and " " not in placa:
            print("Patente registrada correctamente")
            cumple = True
        else:
            print("La patente no puede contener espacios y debe tener al menos 6 caracteres")
    capacidad = 0
    while capacidad <= 0:
        try:
            capacidad = int(input("capacidad de carga del vehiculo (pesado/ligero)"))
            if capacidad <= 0:
                raise ValueError
        except ValueError:
            print("ingrese un numero entero positivo para la capacidad de carga")
            if capacidad > 55:
                pesados += 1
            else:
                ligeros = ligeros +1
    print(f"la flota cuenta con {pesados} vehiculos pesados y {ligeros} vehiculos ligeros rutas asignadas")

    


