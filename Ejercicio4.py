nombre = input ("ingresa el nombre: ")
carrera = input ("ingresa tu carrera: ")
codigo = input ("ingresa el codigo de asignatura: ")

print ("==== Perfil del estudiante ====")
print(f"nombre: {nombre.upper()}")
print(f"concatenado: {carrera[0]+codigo[-1]}")
print(f"cantidad de letras: {len(carrera)}")