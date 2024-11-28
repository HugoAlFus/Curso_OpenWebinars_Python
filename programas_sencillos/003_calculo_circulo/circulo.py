import math

radio = float(input("Introduzca el radio de la circunferencia:"))


def calcular_perimetro():
    return 2 * math.pi * radio


def calcular_area():
    return math.pi * math.pow(radio, 2)


print("El perímetro de un circulo de radio %.2f es de %.2f" % (radio, calcular_perimetro()))
print("El area de un circulo de radio %.2f es de %.2f" % (radio, calcular_area()))
