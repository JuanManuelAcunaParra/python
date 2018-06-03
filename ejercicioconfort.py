print "El confort vale 1000 pesos, con un descuento de 15% si se compra entre 1 y 4, 20% entre 5 y 9 o 25% si son mas de 10"
p=1000
n = int(input("Ingrese la cantidad de conforts a comprar: "))
if n > 9:
    descuento = 0.25 * p
    total=p-descuento
elif n < 10 and n > 4:
    descuento = 0.20 * p
    total=p-descuento
elif n < 5 and n >= 1:
    descuento = 0.15 * p
    total=p-descuento
else:
    total=p

print("El total a pagar es: " ,total*n)