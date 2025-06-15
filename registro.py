import time

def registrar_agregado(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("AGREGADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("Registro.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de agregado guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def registrar_eliminado(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("ELIMINADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("Registro.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de eliminación guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def registrar_modificado(tipo, nombre, apellido, dni):
    fecha_hora = time.ctime()
    tupla = ("MODIFICADO", tipo, nombre, apellido, dni, fecha_hora)
    try:
        with open("Registro.txt", "a") as archivo:
            archivo.write(f"{tupla}\n")
        print("Registro de modificación guardado.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def leer_modificaciones():
    try:
        with open("Registro.txt", "r") as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                print(linea.strip())
    except FileNotFoundError:
        print("No hay modificaciones registradas todavía.")

# Comentario: es necesario agregar abajo de las funciones que agregan, modifican o eliminan personas
# estas funciones con sus parametros. Ejemplo: 
"""
def añadir_alumno():
    if validar.valid_archivo(cursos.archivo):
        with open(cursos.archivo, "r", encoding="UTF-8") as j:
            datos = json.load(j)
        for i in datos:
            if len(i['alumnos']) <= i['max alumnos']:
                print("\n" + "=" * 50)
                print(f"{"» Introduzca el curso donde desea añadir «".center(50)}")
                print("-" * 50)
                curso = menu_texto.seleccion_curso()
                turno = menu_texto.seleccion_turno()
                for i in datos:
                    if curso == i['nombre'] and turno == i['turno']:
                        i['alumnos'].append(cargar_esqueleto())
                        
                        ESTA ES LA PARTE AGREGADA:

                        -------------------------------------------------------------------------------------------
                        alumno = cargar_esqueleto()
                        registrar_agregado("Alumno", alumno['nombre'], alumno['apellido'], alumno['dni'])
                        -------------------------------------------------------------------------------------------

                        break
                otros.cargar_archivo_json(cursos.archivo, datos)
                print('='*50)
                input('Se ha ingresado correctamente al alumno\nPresione Enter para continuar')
                break
            else:
                print('Se ha alcanzado el tope de alumnos establecidos')
                print('Elimine algún alumno o cambie el límite')
                input('Ingrese Enter para continuar')
                break
"""