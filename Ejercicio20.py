num = int(input("Ingrese un numero "))

acumulador = 0
x = 1
while x <= num:
    acumulador = acumulador + x
    x = x + 1
print(acumulador)