print(" ¡Bienvenido al sistema de gestlocalidades del Teatro Municipal!")
max_localidades = 200
cantidad_disponible = 200
historial = 0
opcion = 0
while opcion != 5:
    print("******* MENU PRINCIPAL *******")
    print("1.- Localidades disponibles")
    print("2.- Vender localidades")
    print("3.- Devolver localidades")
    print("4.- Historial de ventas")
    print("5.- Salir")
    print("*********************************")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Debe seleccionar una opcion del 1 al 5")

    if opcion == 1:
        print(f"Entradas disponibles: {cantidad_disponible}")
    elif opcion == 2:
        try:
            compra = int(input("Ingrese la cantidad de localidades a vender: "))
        
            if compra >= 0:
                print("Debe cinorar al menos una entrada")
            elif compra > cantidad_disponible:
                print("No hay suficientes localidades disponibles")
            else: 
                
                cantidad_disponible = cantidad_disponible - compra
                historial = historial + compra

        except ValueError:
            print("Debe ingresar numeros")
    elif opcion == 3:
        try:
            devolucion = int(input("Cuantas localidades devolvera: "))
            if devolucion <= 0:
                print("Debe devolver al menos una localidad")
            elif devolucion + cantidad_disponible > max_localidades:
                print("No se puede devolver, excede el maximo de entradas totales")
            else:
                cantidad_disponible = cantidad_disponible - devolucion
                historial = historial - devolucion
        except ValueError:
            print("Deben ser numeros")
    elif opcion == 4:
        print(f"Cantidad de localidades vendias hasta ahora: {historial}")
    elif opcion == 5:
        print("Gracias por usar nuestro software, hasta la proxima")
    else:
        print("Debe seleccionar una opcion del 1 al 5")