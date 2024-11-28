num1 = float(input("Introduzca el número 1: "))
num2 = float(input("Introduzca el numero 2: "))


def calculo_suma():
    return num1 + num2


def calculo_resta():
    return num1 - num2

def calculo_multipliacion():
    return num1 * num2

def calculo_division():
    return num1 / num2


print("La suma de los numeros %.2f y %.2f es %.2f" % (num1, num2, calculo_suma()))
print("La resta de los numeros %.2f y %.2f es %.2f" % (num1, num2, calculo_resta()))
print("La multiplicacion de los numeros %.2f y %.2f es %.2f" % (num1, num2, calculo_multipliacion()))
print("La divison de los numeros %.2f y %.2f es %.2f" % (num1, num2, calculo_division()))
