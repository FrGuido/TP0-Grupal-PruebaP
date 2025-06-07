import validar
import otros
import menu_texto
import alumnos


import json

nros_cursos = ('1ero', '2do','3ero','4to','5to','6to')

archivo = 'cursos.json'

def modificar_curso():
    if validar.valid_archivo(archivo):
        print('Que curso desea editar?')
        c = menu_texto.opciones_tipos_cursos()
        print('-'*15,'\n')
        t = menu_texto.seleccion_turno()

        with open(archivo, 'r', encoding="UTF-8") as j:
            datos = json.load(j)
        
        for i in datos:
            if i['nombre'] == c and i['turno'] == t:
                while True:
                    opcion = menu_texto.opciones_curso()

                    if opcion == '0':
                        break
                    
                    elif opcion == '1':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando Cantidad Alumnos ~".center(50)}')
                        print("-" * 50)
                        i['max alumnos'] = validar.valid_cant_alumnos(i['max alumnos'], len(i['alumnos']))

                    elif opcion == '2':
                        print("\n" + "=" * 50)
                        print(f'{"~ Modificando Materias ~".center(50)}')
                        print("-" * 50)
                        i['materias'] = validar.valid_nombre()




    else:
        menu_texto.error_archivo()






