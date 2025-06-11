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
                    opcion = menu_texto.opciones_modificar_curso()

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
                        i['materias'] = modificar_materias(i['materias'])




    else:
        menu_texto.error_archivo()





def modificar_materias(lista):
    print('Desea [1] añadir o [2] eliminar una materia?')
    print('Ingrese 0 para salir')
    opcion = input('>>')
    if opcion == '0':
        return lista
    if opcion == '1':
        if len(lista) < 10:
            while True:
                nombre,codigo = menu_texto.elegir_materia()
                for i in lista:
                    if codigo in i:
                        print('Esta materia ya esta en este Curso, elija otra')
                else:
                    lista.append([codigo,nombre])
                    return lista
        else:
            print('Se ha llegado al tope de materias, elimine una para poder añadir')
            return lista
    
    elif opcion == '2':
        if len(lista) > 0:
            while True:
                print('Este es el listado de materias de este curso')
                for i in lista:
                    print(f'Materia: {i[0]} | Codigo: {i[1]}')
                print('-'*20)
                codigo = input('Ingrese el codigo de alguna materia de la lista para eliminar\n>>')
                for i in lista:
                    if codigo in i:
                        lista.remove([codigo,nombre])
                else:
                    print('No ha ingresado un codigo correcto')
                    return lista











