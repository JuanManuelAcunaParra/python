from random import *
x = 0
i = 0
while True:
    x = randint (1,6)
    print (x)
    i = 1 + i
    if x ==5:
        break
    

print("El lanzamiento en el que el que salio el numero 5 fue:" , i)