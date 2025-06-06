import validar
import otros
import texto_menus

import json


cursos = ('1ro', '2do', '3ro', '4to', '5to', '6to')

archivo = 'cursos.json'


def crear_curso():
    curso = {}
    curso['nombre'] = texto_menus.opciones_tipos_cursos()
    curso['cantidad alumnos'] = int(input())
    curso['alumnos'] = []
    curso['materias'] = []
    curso['turno'] = texto_menus.seleccion_turno()
    with open (archivo, 'r', encoding="UTF-8") as j:
        datos = json.load(j)
    datos.append(curso)

    otros.cargar_archivo_json(archivo,datos)


crear_curso()

    









