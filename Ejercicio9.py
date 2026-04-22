curso = (input("Estas cursando 2do año o superior? (si/no) "))
curso = curso.lower()

arancel = (input("Tienes pagado el arancel? (si/no) "))
arancel = arancel.lower()

suspendido = (input("Estas suspendido? (si/no) "))
suspendido = suspendido.lower()

if curso == "si" and arancel == "si" and suspendido == "no" :
        print ("Acceso permitido")
else:
        print ("Acceso denegado")