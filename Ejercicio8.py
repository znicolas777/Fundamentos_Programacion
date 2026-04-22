nota = float(input("ingresa tu nota "))

if nota >= 1.0 and nota <= 3.9:
    print("Reprobado")
elif nota >= 4.0 and nota <= 5.1:
    print("Aprobado")
elif nota >= 5.2 and nota <= 6.5:
    print("Excelente nota")
elif nota >= 6.6 and nota <= 7.0:
    print("Aprobado con honor")
else:
    print("Calificacion ingresada invalida")
