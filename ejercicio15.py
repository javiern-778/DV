total_compra = float (input("ingrese el total de tu compra: "))
if total_compra >100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print (f"¡Felicidades! Tines un descuento del 10%. el total a pagar es {total_final}")
else:
    print(f"El totala pagar es: {total_compra}")