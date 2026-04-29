nombre = input ("Ingrese su nombre ").upper()
años = int (input ("Cuantos años de experiencia tienes? "))
ingles = input ("Que nivel de ingles tienes ? (basico/intermedio/avanzado) ").lower()
viajar = input ("Tienes disponibilidad para viajar? (si/no) ").lower()


if años  >= 5 and ingles == "avanzado":
    print("Postulante destacado - pasa a entrevista final")
elif años  >= 3 and (ingles == "intermedio" or "avanzado") :
    print("Postulante apto -pasa a 2da fase ")
elif viajar == "si" and años >= 1 :
    print("Postulante en revision")
else: 
    print("Postulante no cumple requisitos")

print(f"nombre postulante: {nombre} y cantidad de letras {len(nombre)} ")
