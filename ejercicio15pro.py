nombre =input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto:")
total_compra = float (input("ingrese el total de tu compra: "))

if total_compra > 1000:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print (f"¡Felicidades {nombre}! Tines un descuento del 10%. de tu producto {producto} ")
    print (f"El total a pagar es es {total_final}")
else:
    print(f"El totala pagar es: {total_compra}")