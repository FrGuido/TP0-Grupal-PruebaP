import menu_texto
import validar
import otros
import cursos
import materias

import json




def cargar_esqueleto():
    alu = {}
    print("\n" + "=" * 50)
    print(f"{"» Introduzca su nombre «".center(50)}")
    print("-" * 50)
    alu['nombre'] = validar.valid_nombre()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su apellido «".center(50)}")
    print("-" * 50)
    alu['apellido'] = validar.valid_nombre()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su fecha de nacimiento «".center(50)}")
    print("-" * 50)
    alu['fecha_nacimiento'] = validar.valid_fecha()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su DNI «".center(50)}")
    print("-" * 50)
    alu['dni'] = validar.valid_dni_inalu()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Etapa «".center(50)}")
    print("-" * 50)
    alu['etapa'] = menu_texto.seleccion_etapa()


    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Turno «".center(50)}")
    print("-" * 50)
    alu['turno'] = menu_texto.seleccion_turno()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca un Telefono «".center(50)}")
    print(f"{"para la comunicacion con los padres".center(50)}")
    print("-" * 50)
    alu['telefono'] = validar.valid_telefono()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Contraseña «".center(50)}")
    print("-" * 50)
    alu['pasw'] = validar.valid_pasw()

    return alu

def añadir_alumno():
    if validar.valid_archivo(cursos.archivo):
        with open(cursos.archivo, "r", encoding="UTF-8") as j:
                datos = json.load(j)
        for i in datos:
            if len(i['alumnos']) >= i['max_alumnos']:
                print("\n" + "=" * 50)
                print(f"{"» Introduzca el curso donde desea añadir «".center(50)}")
                print("-" * 50)
                curso = menu_texto.seleccion_curso()
                for i in datos:
                    if curso == i['nombre']:
                        i['alumnos'].append(cargar_esqueleto())
                otros.cargar_archivo_json(cursos.archivo,datos)
                print('='*50)
                input('Se ha ingresado correctamente al alumno\nPresione Enter para continuar')
                break
            else:
                print('Se ha alcanzado el tope de alumnos establecidos')
                print('Elimine algun alumno o cambie el limite')
                input('Ingrese Enter para continuar')
                break


    else:
        menu_texto.error_archivo()

def buscar_alumno(dni):
    with open(cursos.archivo,'r',encoding="UTF-8") as j:
        datos = json.load(j)
        for i in datos:
            for j in i['alumnos']:
                if j['dni'] == dni:
                    return j
        else:
            print('No se encontro al alumno de ese DNI\n')
            return None

def modificar_alumno():
    if validar.valid_archivo(cursos.archivo):
        while True:
            dni = otros.pedir_dni()
            alu = buscar_alumno(dni)
            if alu == None:
                print('Desea intentarlo de nuevo?')
                vl = menu_texto.confirmacion_user()
                if vl == 'n':
                    return
            else:
                break
            
        print('Este es el alumno que esta editando\n')
        menu_texto.imprimir_dic(alu)
        input('Ingrese enter para continuar')            

        with open(cursos.archivo,'r',encoding="UTF-8") as j:
            datos = json.load(j)
        for i in datos:
            for j in i['alumnos']:
                if j['dni'] == dni:
                    while True:
                        opcion = menu_texto.opcion_modificar_alumno()

                        if opcion == '0':
                            break
                        
                        elif opcion == '1':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando nombre ~".center(50)}')
                            print(f"{"» Introduzca su nuevo nombre «".center(50)}")
                            print("-" * 50)
                            j['nombre'] = validar.valid_nombre()

                        elif opcion == '2':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando apellido ~".center(50)}')
                            print(f"{"» Introduzca su nuevo apellido «".center(50)}")
                            print("-" * 50)
                            j['apellido'] = validar.valid_nombre()

                        elif opcion == '3':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando fecha de nacimiento ~".center(50)}')
                            print(f"{"» Introduzca su nueva fecha «".center(50)}")
                            print("-" * 50)
                            j['fecha_nacimiento'] = validar.valid_fecha()

                        elif opcion == '4':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando DNI ~".center(50)}')
                            print(f"{"» Introduzca su DNI «".center(50)}")
                            print("-" * 50)
                            j['dni'] = validar.valid_dni_inalu()
                        
                        elif opcion == '5':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando Etapa ~".center(50)}')
                            print(f"{"» Introduzca su nueva Etapa «".center(50)}")
                            print("-" * 50)
                            j['etapa'] = menu_texto.seleccion_etapa()

                        elif opcion == '7':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando Turno ~".center(50)}')
                            print(f"{"» Introduzca su nuevo Turno «".center(50)}")
                            print("-" * 50)
                            j['turno'] = menu_texto.seleccion_turno()

                        elif opcion == '8':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando Email ~".center(50)}')
                            print(f"{"» Introduzca su nuevo Email «".center(50)}")
                            print("-" * 50)
                            j['mail'] = validar.valid_mail()

                        elif opcion == '9':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando telefono ~".center(50)}')
                            print(f"{"» Introduzca su nuevo Telefono «".center(50)}")
                            print("-" * 50)
                            j['telefono'] = validar.valid_telefono()

                        elif opcion == '10':
                            print("\n" + "=" * 50)
                            print(f'{"~ Modificando Contraseña ~".center(50)}')
                            print(f"{"» Introduzca su nueva Contraseña «".center(50)}")
                            print("-" * 50)
                            j['pasw'] = validar.valid_pasw()
                    break

        otros.cargar_archivo_json(cursos.archivo,datos)
    else:
        menu_texto.error_archivo()

    input('Volviendo al menu inicial, precione enter')

def eliminar_alumno():
    if validar.valid_archivo(cursos.archivo):
        while True:
            try:
                dni = int(input('Ingrese el DNI del alumno a eliminar\n>> '))
                with open(cursos.archivo,'r',encoding="UTF-8") as j:
                    datos = json.load(j)
                print('ESTA POR ELIMINAR EL ALUMNO')
                for i in datos:
                    for j in i['alumnos']:
                        if j['dni'] == dni:
                            print(f'DEL CURSO {i['nombre']}')
                            print('='*10)
                            menu_texto.imprimir_dic(j)
                            print('\nSeguro que desea eliminar este elemento?\n')
                            seg = menu_texto.confirmacion_user()
                            if seg == 's':
                                i['alumnos'] = list(filter(lambda x: x['dni'] != dni, i['alumnos']))
                                otros.cargar_archivo_json(cursos.archivo,datos)
                                print('='*50)
                                input('Se ha eliminado correctamente al alumno\nPresione Enter para continuar')
                                return
                            else:
                                input('Volviendo al menu inicial, precione enter')
                                return

            except:
                print('Ingrese numeros\n--------------')
    else:
        menu_texto.error_archivo()

def modificar_notas_alumno():
    if validar.valid_archivo(cursos.archivo):
        while True:
            dni = otros.pedir_dni()
            alu = buscar_alumno(dni)
            if alu == None:
                print('Desea intentarlo de nuevo?')
                vl = menu_texto.confirmacion_user()
                if vl == 'n':
                    return
            else:
                break
            
        print('Este es el alumno del que esta editando/viendo sus notas\n')
        menu_texto.imprimir_dic(alu)
        input('Ingrese enter para continuar')
        with open(cursos.archivo,'r',encoding="UTF-8") as j:
            datos = json.load(j)
        for i in datos:
            for j in i['alumnos']:
                if j['dni'] == dni:
                    pass



    else:
        menu_texto.error_archivo()
    input('Volviendo al menu inicial, precione enter')



def añadir_nota(alumno):
    with open(materias.archivo,"r", encoding="UTF-8") as j:
        datos = json.load(j)
    for i in datos:
        menu_texto.imprimir_dic(i)

    while True:
        print('De que materia es la nota que se esta ingresando?')
        materia = menu_texto.elegir_materia()
        
            















