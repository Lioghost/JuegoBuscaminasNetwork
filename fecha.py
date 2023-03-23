import datetime
# Necesitamos el día, mes y año
dia = int(input("Día de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
anio = int(input("Año de nacimiento: "))


fecha_de_nacimiento = datetime.datetime(anio, mes, dia)

dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

fecha_de_inicio = datetime.datetime(anio, mes, dia)

diferencia = fecha_de_inicio - fecha_de_nacimiento

dias_vividos = diferencia.days

segundos_vividos = diferencia.seconds

horas_vividas, segundos_vividos = divmod(segundos_vividos, 3600)

minutos_vividos, segundos_vividos = divmod(segundos_vividos, 60)

# Preparar un mensaje
mensaje = "Has vivido {} día(s), {} hora(s), {} minuto(s) y {} segundo(s)".format(
    dias_vividos, horas_vividas, minutos_vividos, segundos_vividos)

print(mensaje)

print("Practica: ", 8652 % 3)