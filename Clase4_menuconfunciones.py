def menu():
    print ("1. Primera opcion")
    print ("2. Segunda opcion")
    print ("3. Tercera opcion")
    print ("4. Salir")
while True:
    menu()
    opcionMenu = input("Inserta una opcion: ")
    if opcionMenu == 1:
        print (" ")
        input("Has pulsado la opcion 1. Pulsa una tecla para continuar")
    elif opcionMenu == 2:
        print (" ")
        input("Has pulsado la opcion 2. Pulsa una tecla para continuar")
    elif opcionMenu == 3:
        print (" ")
        input("Has pulsado la opcion 3. Pulsa una tecla para continuar")
    elif opcionMenu == 4:
        break
    else:
        print (" ")
        input("No has pulsado ninguna opcion correcta. Pulsa una tecla para continuar")
        