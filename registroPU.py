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
                print(linea.strip())
    except FileNotFoundError:
        print("No hay modificaciones registradas todavía.")