import validar
import menu_texto
import otros


import json




archivo  = "materias.json"


def cargar_esqueleto():
    mat={}
    print("\n" + "=" * 50)
    print(f"{"» Introduzca el nombre «".center(50)}")
    print("-" * 50)
    mat['nombre'] = validar.valid_repeticion_nombre(validar.valid_nombre())

    print("\n" + "=" * 50)
    print(f"{"» Introduzca los profesores a cargo «".center(50)}")
    print("-" * 50)
    mat['profesores'] = validar.prof_acargo()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca el codigo de identificacion de la materia «".center(50)}")
    print("-" * 50)
    mat['codigo'] = validar.valid_codigo_materia()

def crear_materia():
    if validar.valid_archivo(archivo):
        with open(archivo, "r", encoding="UTF-8") as j:
            try:
                datos = json.load(j)
            except json.JSONDecodeError:
                datos = []
        
        datos.append(cargar_esqueleto())

        otros.cargar_archivo_json(archivo, datos)
        print('='*50)
        input('Se ha ingresado correctamente la materia\nPresione una tecla para continuar')

    else:
        menu_texto.error_archivo()

def modificar_materia():
    if validar.valid_archivo(archivo):
        pass
    else:
        menu_texto.error_archivo()








