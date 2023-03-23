import datetime
# Necesitamos el día, mes y año
dia = int(input("Día de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
anio = int(input("Año de nacimiento: "))

# Crear un objeto de tipo datetime.datetime; con horas, minutos y segundos en 0
fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
# Necesitamos la fecha y hora de hoy...
fecha_de_hoy = datetime.datetime.now()
# Operar como si fueran simples números
diferencia = fecha_de_hoy - fecha_de_nacimiento
# Y ahora podemos acceder a cada valor por separado ;)
# Es un objeto timedelta: https://docs.python.org/3/library/datetime.html#timedelta-objects
dias_vividos = diferencia.days
# Para los minutos y horas es distinto
segundos_vividos = diferencia.seconds
# Convertir segundos a horas y obtener sobrante
horas_vividas, segundos_vividos = divmod(segundos_vividos, 3600)
# Convertir segundos sobrantes a minutos y obtener sobrante
minutos_vividos, segundos_vividos = divmod(segundos_vividos, 60)

# Preparar un mensaje
mensaje = "Has vivido {} día(s), {} hora(s), {} minuto(s) y {} segundo(s)".format(
    dias_vividos, horas_vividas, minutos_vividos, segundos_vividos)
# Imprimirlo y listo
print(mensaje)