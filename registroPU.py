import time

def registrar_agregadoPU(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("AGREGADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("RegistroPU.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de agregado guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def registrar_eliminadoPU(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("ELIMINADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("RegistroPU.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de eliminación guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def registrar_modificadoPU(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("MODIFICADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("RegistroPU.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de modificación guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def leer_modificacionesPU():
    try:
        with open("RegistroPU.txt", "r") as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                linea = linea.strip()

                if linea.startswith("(") and linea.endswith(")"):
                    linea = linea[1:-1]

                partes = linea.split(",", 5)

                if len(partes) == 6:
                    accion   = partes[0].strip().strip("'")
                    tipo     = partes[1].strip().strip("'")
                    nombre   = partes[2].strip().strip("'")
                    apellido = partes[3].strip().strip("'")
                    dni      = partes[4].strip()
                    fecha    = partes[5].strip().strip("'")

                    print(f"""
Acción     : {accion}
Tipo       : {tipo}
Nombre     : {nombre}
Apellido   : {apellido}
DNI        : {dni}
Fecha      : {fecha}
                    """)
                else:
                    print(f"Línea malformada: {linea}")
    except FileNotFoundError:
        print("No hay modificaciones registradas todavía.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")