#PRIMERA PARTE ELIGE EL DESCUENTO PARA VIAJAR EN AUTOBUS
print("BIENVENIDO A LA CENTRAL DE AUTOBUSES")

edad = int(input("Escribe tu edad: "))
tipo_carnet = input("Elige el tipo de tarjeta: "
                    "Niño N / Profesor P / "
                    "Estudiante E / INAPAM I"
                    "Ninguno NA ")

if edad <= 12 and tipo_carnet == "N" \
        or tipo_carnet == "P" \
        or 17 <= edad <= 35 and tipo_carnet == "E" \
        or edad >= 60 and tipo_carnet == "I":
    print("TIENE DESCUENTO")
else:
    print("NO TIENE DESCUENTO")

#SEGUNDA PARTE ELIGE EL ASIENTO DEL AUTOBUS VAMOS A TRABAJAR CON EXCEL Y OTRAS LIBRERIAS