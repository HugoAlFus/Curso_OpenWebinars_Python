base = float(input("Introduzca la base del triangulo: "))
altura = float(input("Introduzca la altura del triangulo: "))


def calcular_perimetro():
    return (1 / 2) * base * altura


def calcular_area():
    return (base * altura) / 2


print("El perímetro de un triangulo de base %.2f y altura %.2f es de %.2f" % (base, altura, calcular_perimetro()))
print("El área de un triangulo de base %.2f y altura %.2f es de %.2f" % (base, altura, calcular_area()))
