
minutos =int(input("Introduzca la cantidad de minutos: "))
horas_completas = minutos // 60
minutos_restantes = minutos %60

print("Horas: %d - Minutos: %d" % (horas_completas, minutos_restantes))
