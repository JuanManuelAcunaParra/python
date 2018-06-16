cadena = "abcdefghijklmnopqrstuvwxyz"
i = 0
for i in range(len(cadena)):
    if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
        print cadena[i] + " Vocal"
