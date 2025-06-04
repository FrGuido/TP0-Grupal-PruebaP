import validar
import texto_menus
import json

archivo = 'profesores.json'

def cargar_archivo_json(ruta,datos):
    with open(ruta, "w", encoding="UTF-8") as j:
        json.dump(datos, j, indent=2, ensure_ascii=False)

def cargar_esqueleto():
    prof = {}
    print("\n" + "=" * 50)
    print(f"{"» Introduzca su nombre «".center(50)}")
    print("-" * 50)
    prof['nombre'] = validar.valid_nombre()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su apellido «".center(50)}")
    print("-" * 50)
    prof['apellido'] = validar.valid_nombre()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su fecha de nacimiento «".center(50)}")
    print("-" * 50)
    prof['fecha_nacimiento'] = validar.valid_fecha()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su DNI «".center(50)}")
    print("-" * 50)
    prof['dni'] = validar.valid_dni(archivo)

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Email «".center(50)}")
    print("-" * 50)
    prof['mail'] = validar.valid_mail()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Telefono «".center(50)}")
    print("-" * 50)
    prof['telefono'] = validar.valid_telefono()

    print("\n" + "=" * 50)
    print(f"{"» Introduzca su Contraseña «".center(50)}")
    print("-" * 50)
    prof['pasw'] = validar.valid_pasw()

    return prof


def añadir_profesor():

    if validar.valid_archivo(archivo):
        with open(archivo, "r", encoding="UTF-8") as j:
            try:
                datos = json.load(j)
            except json.JSONDecodeError:
                datos = []
        datos.append(cargar_esqueleto())

        cargar_archivo_json(archivo,datos)

        print('='*50)
        input('Se ha ingresado correctamente al profesor\nPresione una tecla para continuar')

    else:
        texto_menus.error_archivo()


def buscar_profesor(dni):
    with open('profesores.json','r',encoding="UTF-8"):
        datos = json.load()
        for i in datos:
            if i['dni'] == dni:
                return i
        else:
            print('No se encontro al profesor de ese DNI\n')


def modificar_profesor():
    if validar.valid_archivo(archivo):
        pass
    else:
        texto_menus.error_archivo()


def eliminar_profesor():
    if validar.valid_archivo(archivo):
        while True:
            try:
                dni = int(input('Ingrese el DNI del profesor a eliminar\n>> '))
                seg = texto_menus.confirmacion_user()
                if seg == 's':
                    with open(archivo,'r',encoding="UTF-8") as j:
                        datos = json.load(j)

                    datos = list(filter(lambda x: x['dni'] != dni, datos))
                    
                    cargar_archivo_json(archivo,datos)

                    print('='*50)
                    input('Se ha eliminado correctamente al profesor\nPresione una tecla para continuar')


                    break

                else:
                    break

            except:
                print('Ingrese numeros\n--------------')

    else:
        texto_menus.error_archivo()

#añadir_profesor()
#eliminar_profesor()





































