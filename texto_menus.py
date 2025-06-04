def bienvenida():
    print('\n'*10)
    print(f'{" Bienvenido al sistema de alumnado © ":-^58}')
    print(f'{"Trabajo Practico - Programacion 1":^58}')
    print(f'{"Grupo 10":^58}')
    print(f'{" - "*15:^58}')


def opciones_principal():
    while True:
        opciones = 4
        print()
        print("-" * 26)
        print("MENÚ PRINCIPAL")
        print("-" * 26)
        print("[1] Gestión de profesores")
        print("[2] Gestión de alumnos")
        print("[3] Gestión de materias")
        print("[4] Registro de cambios")
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





