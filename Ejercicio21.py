opcion = 0
while opcion != 4:
    print("**** MENU PRINCIPAL ****")
    print("1.- Sumar")
    print("2.- Restar ")
    print("3.- Multiplicar")
    print("4.- Salir")
    opcion = int(input("Seleccione una opción: "))
    #valido que opcion seleccionó
    if opcion == 1:
        #realizo la suma
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        #realizo la suma
        total = n1 + n2
        print(f"La suma es {total}")
    elif opcion == 2:
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        #realizo la resta
        total = n1 - n2
        print(f"La resta es {total}")
    elif opcion == 3:
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        #realizo la multi
        total = n1 * n2
        print(f"La multiplicación es {total}")
    elif opcion == 4:
        print("Gracias por usar el sistema")
    else:
        print("Opción seleccionada incorrecta")