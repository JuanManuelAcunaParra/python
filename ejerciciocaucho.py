n = int(input("Ingrese la cantidad de cauchos a comprar: "))
p = float(input("Ingrese el precio unitario: "))
if n > 6:
    descuento = 0.15 * p
    total=p-descuento
else:
    descuento = 0.1 * p
    total=p-descuento


print("El total a pagar es: " ,total*n)