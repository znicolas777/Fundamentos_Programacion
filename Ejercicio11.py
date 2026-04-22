temperatura = float(input ("Ingrese la temperatura actual "))

if temperatura < 10 :
    print ("Frio")
elif temperatura >= 10 and temperatura <= 25:
    print ("Templado")
else:
    print("Caluroso")