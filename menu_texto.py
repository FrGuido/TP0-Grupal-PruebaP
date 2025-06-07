import cursos
import materias
import profesores
import json


def bienvenida():
    print('\n'*10)
    print(f'{" Bienvenido al sistema de alumnado © ":-^58}')
    print(f'{"Trabajo Practico - Programacion 1":^58}')
    print(f'{"Grupo 10":^58}')
    print(f'{" - "*15:^58}')


def opciones_principal():
    while True:
        opciones = 5
        print()
        print("-" * 26)
        print("MENÚ PRINCIPAL")
        print("-" * 26)
        print("[1] Gestión de profesores")
        print("[2] Gestión de alumnos")
        print("[3] Gestion de cursos")
        print("[4] Gestion de materias")
        print("[5] Registro de cambios")
        print("-" * 26)
        print("[0] Salir del programa")
        print("-" * 26)
        print()

        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()
    return opcion


def opciones_profesores():
    while True:
        opciones = 5
        print()
        print("---------------------------")
        print("MENÚ PRINCIPAL > GESTION DE PROFESORES")
        print("---------------------------")
        print("[1] Añadir Profesores")
        print("[2] Eliminar Profesor")
        print("[3] Modificar Profesor")
        print("[4] Modificar Materias Profesor")
        print("[5] Lista Profesores")
        print("---------------------------")
        print("[0] Volver al menú anterior")
        print("---------------------------")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()
    return opcion


def opcion_modificar_profesor():
    while True:
        opciones = 7
        print(f'Que desea modificar?')
        print("---------------------------")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] Fecha de Nacimiento")
        print("[4] DNI")
        print("[5] Mail")
        print("[6] Telefono")
        print("[7] Contraseña")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def opcion_modificar_alumno():
    while True:
        opciones = 10
        print(f'Que desea modificar?')
        print("---------------------------")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] Fecha de Nacimiento")
        print("[4] DNI")
        print("[5] Etapa")
        print("[6] Curso")
        print("[7] Turno")
        print("[8] Mail")
        print("[9] Telefono")
        print("[10] Contraseña")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def opciones_curso():
    while True:
        opciones = 2
        print(f'Que desea modificar?')
        print("---------------------------")
        print("[1] Cantidad Maxima de Alumnos")
        print("[2] Materias")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def opciones_materias():
    while True:
        opciones = 2
        print(f'Que desea modificar?')
        print("---------------------------")
        print("[1] Cantidad Maxima de Alumnos")
        print("[2] Materias")
        print("---------------------------")
        print("[0] Salir")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            return opcion
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")


def lista_profesores_disponibles():
    print('Esta es la lista de profesores disponibles')
    with open(profesores.archivo, "r", encoding="UTF-8") as j:
        datos_p = json.load(j)

    with open(materias.archivo, "r", encoding="UTF-8") as j:
        datos_m = json.load(j)

    disponibles = []

    for i in datos_p:
        contador = 0
        for j in datos_m:
            for h in j['profesores']:
                if i['dni'] == h[0]:
                    contador += 1
        if contador < 3:
            disponibles.append([i['dni'],i['nombre']])
            print('=' * 52)
            print(f'| {str(i['nombre']):<20} DNI {str(i['dni']):>25} |')
    print('=' * 52)
    return disponibles


def opciones_alumno():
    while True:
        opciones = 5
        print()
        print("---------------------------")
        print("MENÚ PRINCIPAL > GESTION DE ALUMNOS")
        print("---------------------------")
        print("[1] Añadir Alumno")
        print("[2] Eliminar Alumno")
        print("[3] Modificar Alumno")
        print("[4] Modificar Notas Alumno")
        print("[5] Listar Alumnos Curso")
        print("---------------------------")
        print("[0] Volver al menú anterior")
        print("---------------------------")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()
    return opcion


def opciones_tipos_cursos():
    print('Elija una de las siguientes opciones')
    opciones = len(cursos.nros_cursos)
    while True:
        print('-'*15)
        for i,e in enumerate(cursos.nros_cursos):
            print(f'[{i+1}] {e}')
        print('-'*15)
        opcion = input('>>')
        if opcion in [str(i) for i in range(1, opciones+1)]:
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == '1':
        return cursos.nros_cursos[0]
    elif opcion == '2':
        return cursos.nros_cursos[1]
    elif opcion == '3':
        return cursos.nros_cursos[2]
    elif opcion == '4':
        return cursos.nros_cursos[3]
    elif opcion == '5':
        return cursos.nros_cursos[4]
    elif opcion == '6':
        return cursos.nros_cursos[5]


def error_archivo():
    print()
    print('!','='*15,'!')
    print('No se ha podido acceder al archivo\nVerifique su integridad o existencia')
    print('!','='*15,'!')
    print()


def confirmacion_user():
    while True:
        rta = input('Ingrese "S" para si\nIngrese "N" para no\n>>')
        print()
        if rta.lower() == 's' or rta.lower() == 'n':
            return rta
        else:
            print('Ingrese uno de los valores indicados\n-----------------\n')


def imprimir_dic(dic):
    print('=' * 52)
    for key, valor in dic.items():
        a = f'| {str(key):<20} : {str(valor):>25} |'
        print(a)
    print('-' * 52)


def seleccion_turno():
    while True:
        print('Que turno desea?')
        print('-'*15)
        print('[1] Turno Mañana')
        print('[2] Turno Tarde')
        print('-'*15)
        turno = input('>')
        if turno == '1':
            return 'Mañana'
        elif turno == '2':
            return 'Tarde'
        else:
            print('Ingrese un valor valido, intente de nuevo\n-----------\n')


def seleccion_curso():
    while True:
        print('Que curso desea ingresar?')
        print('-'*15)
        print('[1] Primer Grado/Año')
        print('[2] Segundo Grado/Año')
        print('[3] Tercer Grado/Año')
        print('[4] Cuarto Grado/Año')
        print('[5] Quinto Grado/Año')
        print('[6] Sexto Grado/Año')
        print('-'*15)
        turno = input('>')
        if turno == '1':
            return '1ro'
        elif turno == '2':
            return '2ro'
        elif turno == '3':
            return '3ro'
        elif turno == '4':
            return '4ro'
        elif turno == '5':
            return '5ro'
        elif turno == '6':
            return '6ro'
        else:
            print('Ingrese una opcion valida\n-----------\n')


def seleccion_etapa():
    while True:
        print('Que etapa desea?')
        print('-'*15)
        print('[1] Educacion Primaria')
        print('[2] Educacion Secundaria')
        print('-'*15)
        turno = input('>')
        if turno == '1':
            return 'Primario'
        elif turno == '2':
            return 'Secundario'
        else:
            print('Ingrese un valor valido, intente de nuevo\n-----------\n')





