compra = float(input("Ingrese el monto de su compra: "))
tipo = input("Es cliente VIP (si/no)")

if tipo.lower() == "si" and compra >= 50000:
    #descuento 25%
    descuento = (compra * 25) / 100
    total = compra - descuento
    print(f"Se aplica un 25% de descuento: ${descuento}")
    print(f"Su total a pagar es ${total}")
elif tipo.lower() == "si" and compra < 50000:
    #descuento 15%
    descuento = (compra * 15) / 100
    total = compra - descuento
    print(f"Se aplica un 15% de descuento: ${descuento}")
    print(f"Su total a pagar es ${total}")
elif tipo.lower() == "no" and compra >= 100000:
    #descuento 10%
    descuento = (compra * 10) / 100
    total = compra - descuento
    print(f"Se aplica un 10% de descuento: ${descuento}")
    print(f"Su total a pagar es ${total}")
else:
    print("No posee descuentos")
    print(f"Su total a pagar es ${compra}")