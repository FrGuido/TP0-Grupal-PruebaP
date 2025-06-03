import validar
import texto_menus
import json

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
    prof['dni'] = validar.valid_dni()

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

    archivo = 'profesores.json'

    if validar.valid_archivo(archivo):
        with open(archivo, "r", encoding="UTF-8") as j:
            try:
                datos = json.load(j)
            except json.JSONDecodeError:
                datos = []
        datos.append(cargar_esqueleto())

        with open(archivo, "w", encoding="UTF-8") as j:
            json.dump(datos, j, indent=2, ensure_ascii=False)

    else:
        texto_menus.error_archivo()

añadir_profesor()









































