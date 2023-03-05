import math
pi= math.pi
radioC=float(input("Ingrese radio del circulo: "))
baseT=float(input("Ingrese base del triangulo: "))
alturaT=float(input("Ingrese altura del triangulo: "))
ladoC=float(input("Ingrese lado del cuadrado: "))

AreaCirculo= pi*radioC**2
AreaTriang=(baseT*alturaT)/2
AreaCuad=ladoC**2
print(f"El area del circulo es: {AreaCirculo}")
print(f"El area del triangulo es: {AreaTriang}")
print(f"El area del cuadrado es: {AreaCuad}")
