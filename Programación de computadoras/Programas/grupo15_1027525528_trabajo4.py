""" Grupo 15
    Trabajo 4
    TI: 1027525528
    Nombre: Silvana Suarez Carvajal 
"""

import json
from pprint import pprint
from subprocess import call

call('cls', shell=True)

datos = {
    "Suministros": ["Cables", "CD", "DVD"],
    "Electronicos": [],
    "Software": ["Contabilidad", "Nómina"]
}

try:
    with open("datos0.json", 'w', encoding='utf8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

except FileNotFoundError:
    print("El archivo no se puede crear porque no se encuentra el directorio.")

except PermissionError:
    print("No tienes permisos para crear o sobrescribir el archivo.")

except json.JSONDecodeError as error:
    print("Error de decodificación JSON: ", error)


try:
    with open("datos0.json", "r", encoding='utf8') as archivo:
        datos_leidos = json.load(archivo)

except PermissionError:
    print("No tienes los permisos necesarios para leer el archivo")

except FileNotFoundError:
    print("El archivo no existe.")
    with open("datos0.json", 'w', encoding='utf8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

except TypeError:
    print("Tipo de archivo inválido.")

except ValueError:
    print('Ha fallado la descodificación de JSON')

pprint(datos_leidos)
