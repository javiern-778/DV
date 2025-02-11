import datetime
import random

# Datos de la tienda
nombre_tienda = "Tienda XYZ"
folio = random.randint(1000, 9999)  # Generar un folio único aleatorio
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Datos del cliente y la compra
nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
total_compra = float(input("Ingresa el total de tu compra: "))

# Cálculo del descuento
if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
else:
    descuento = 0
    total_final = total_compra

# Imprimir el ticket de compra
print("=" * 50)
print(" " * 15 + "TICKET DE COMPRA" + " " * 15)
print("=" * 50)
print(f"Tienda: {nombre_tienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha_hora}")
print("-" * 50)
print(f"Cliente: {nombre}")
print(f"Producto: {producto}")
print(f"Total de la compra: ${total_compra:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total_final:.2f}")
print("-" * 50)
print("¡Gracias por tu compra! ¡Vuelve pronto!")
print("=" * 50)
