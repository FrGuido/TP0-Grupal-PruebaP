import json


def cargar_archivo_json(ruta,datos):
    with open(ruta, "w", encoding="UTF-8") as j:
        json.dump(datos, j, indent=2, ensure_ascii=False)

def pedir_dni():
    while True:
        try:
            dni = int(input('Ingrese el DNI\n>>'))
            return dni
        except:
            print('Ingrese numeros\n------------\n')









