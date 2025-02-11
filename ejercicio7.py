import math

#pedir el radio del circulo 
radio= float (input("Introduce el radio del circulo en metros:\n"))

#calcula el area del circulo (A = *R^2)
area = math.pi * (radio ** 2)

#mostrar mensaje 
print (f"\n El area del circulo con radio {radio} metros es: {area:.2f} metros cuadrados.")