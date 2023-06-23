# !/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Módulo os: Proporciona funciones para interactuar con el sistema operativo."""
from subprocess import call
import os

""" Función call: Permite limpiar la pnatalla completamente."""

try:
    from color import Color
except ModuleNotFoundError:  # Al no encontrar el módulo.
    alerta = '''\033[31 No se logró encontar el archivo "color.py" en la ruta por defecto.,
        Tenga en cuenta que debe estar en la misma carpeta que este programa (archivo ".py")'''
    print(alerta)
except ImportError:
    alerta = "\033[31 No se pudo importar el módulo 'color'."
    print(alerta)
# Identificador de otras excepciones posibles (no contempladas).
except Exception as excep:
    alerta = '\033[31 Ocurrió la siguiente excepción: ', type(excep)
    print(alerta)


def listar(linea):
    """ Divide una cadena por comas y devuelve una lista de elementos."""
    lista = linea.split(",")
    return lista


def pretty_print(color, texto):
    """Retorna el texto de el color especificado."""
    if color == "BLUE":
        colorsito = Color.BLUE
    elif color == "GREEN":
        colorsito = Color.GREEN
    elif color == "RED":
        colorsito = Color.RED

    texto_con_color = f'{colorsito}{texto}{Color.RESET}'
    return texto_con_color


def siguiente(proceso='continuar'):
    """Espera a que el usuario presione la tecla Enter y luego limpia la pantalla."""
    texto_input = pretty_print("GREEN", "enter")
    try:
        input(f'\n Presione {texto_input} para {proceso}.\n ')
    except EOFError:  # (Excepción por "ctrl + z" o comandos inesperados)
        pass
    except KeyboardInterrupt:  # (Excepción por "ctrl + c")
        call('cls', shell=True)
        texto_ctrlc = pretty_print("GREEN", "ctrl + c")
        print(f'{Color.RED} Digitó {texto_ctrlc}, el comando para salir del programa.{Color.RESET}\n',
              f'\n  - Presione {texto_input} para salir.')
        try:
            entrada = input(
                f'\n  - Digite cualquier otro valor para continuar viendo el programa.\n ')
        except:
            pass
        else:
            if entrada == '':
                call('cls', shell=True)
                quit()
    call('cls', shell=True)
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("nt"):
        os.system("cls")


def save_in_diccionary(archivo):
    """Lee un archivo y guarda los datos en un diccionario."""
    categorias, datos_archivo = {}, archivo.read().split('\n')
    encabezado = datos_archivo[0].split(',')
    for categoria in encabezado:
        categorias[categoria] = []
    for linea in range(1, len(datos_archivo)):
        elementos = datos_archivo[linea].split(',')
        for elemento, categoria in enumerate(categorias):
            categorias[categoria].append(elementos[elemento])
    return categorias


def titulo(texto, diccionario):
    """Imprime un título subrayado con el texto especificado y centrado"""
    longitud = 5
    for categoria in diccionario:
        longitud += len(categoria) + 5

    titulo_subrayado = f"{Color.SUBRAY}{texto}"
    titulo_subrayado = f"{titulo_subrayado:^{longitud}}"

    print(pretty_print("GREEN", titulo_subrayado))


def separador_vertical(texto="", longitud=0):
    """Genera una cadena con un separador vertical."""
    vertical = pretty_print("BLUE", "|")
    impresion = f"{texto:^{longitud}}{vertical}"
    return impresion


def separador_horizontal(longitud):
    """Genera una línea de separación horizontal."""
    sep = "="*longitud
    impresion_con_linea = f"{sep}."
    return impresion_con_linea


def pretty_encabezado(diccionario):
    """Genera el encabezado formateado de una estructura de datos."""
    texto_encabezado = separador_vertical()
    linea_encabezado = "."
    for categoria in diccionario:
        longitud = len(categoria)+4
        linea_encabezado += separador_horizontal(longitud)
        texto_encabezado += separador_vertical(categoria, longitud)

    linea = pretty_print("BLUE", linea_encabezado)
    texto_intermedio = texto_encabezado

    return linea, texto_intermedio


def pretty_datos(diccionario, largo):
    """Imprime los datos formateados de un diccionario en líneas separadas."""
    for i in range(largo):
        texto_linea = separador_vertical()
        for key in diccionario:
            longitud = len(key)+4
            texto_linea += separador_vertical(diccionario[key][i], longitud)
        print(texto_linea)


def pretty_tabla(diccionario, largo, text):
    """Imprime una tabla formateada con encabezado, título y datos."""
    linea, texto_intermedio = pretty_encabezado(diccionario)
    titulo(text, diccionario)
    print(linea)
    print(texto_intermedio)
    print(linea)
    pretty_datos(diccionario, largo)
    print(linea)


def codigos_sin_repetir(diccionario):
    """Obtiene los códigos de producto únicos y sin repetir de un diccionario."""
    los_id_producto = sorted(set(diccionario["id_producto"]))
    return los_id_producto


def lista_diccionario(categoria, diccionario):
    """Obtiene la lista de valores correspondientes a una categoría en un diccionario."""
    list_dic = diccionario[categoria]
    return list_dic


def precio(indice, diccionario):  # solo funciona si se invoca la anterior primero
    """Obtiene el precio individual correspondiente a un índice en un diccionario."""
    lista_de_precio = lista_diccionario("precio_unitario", diccionario)
    precio_individual = lista_de_precio[indice]
    return precio_individual


def todo_id(diccionario):
    """Obtiene una lista de todos los valores de "id_producto" en un diccionario."""
    lista_de_id = lista_diccionario("id_producto", diccionario)
    return lista_de_id


def cantidades(diccionario):
    """Obtiene una lista de todas las cantidades en un diccionario."""
    toda_cantidad = lista_diccionario("cantidad", diccionario)
    return toda_cantidad


def tabla_inicial(diccionario):
    """Crea una tabla inicial con valores iniciales para diferentes categorías."""
    tablita = {"id_producto": codigos_sin_repetir(diccionario), "número_de_ventas": [
        0]*6, "cantidad_vendida": [0]*6, "precio_unitario": [], "valor_total": []}
    return tablita


def diccionario_especial(diccionario, c_producto):
    """Crea un diccionario especial con información actualizada y cálculos basados en los datos de entrada."""
    dic_inicial = tabla_inicial(diccionario)
    for a, dato in enumerate(c_producto):  # los datos son 1,2,3,4,5 y 6
        indice = todo_id(diccionario).index(dato)
        precio_individual = precio(indice, diccionario)
        dic_inicial["precio_unitario"].append(precio_individual)
        # lista de id es la larga
        for i, llave_producto in enumerate(todo_id(diccionario)):
            if llave_producto == dato:
                venta = cantidades(diccionario)[i]
                dic_inicial["cantidad_vendida"][a] += int(venta)
                dic_inicial["número_de_ventas"][a] += 1
        cantidad = (float(precio_individual)) * \
            (dic_inicial["cantidad_vendida"][a])
        dic_inicial["valor_total"].append(cantidad)
    return dic_inicial


def diccionario_especifico(diccionario, categoria_2, categoria_1="id_producto"):
    """Crea un nuevo diccionario con las categorías especificadas a partir del diccionario original."""
    nuevo_dic = {
        categoria_1: diccionario[categoria_1], categoria_2: diccionario[categoria_2]}
    return nuevo_dic


# Apertura del archivo.

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)

try:
    with open(path+'/datos.txt', 'r', encoding='utf8') as datos:
        ventas = save_in_diccionary(datos)
except FileNotFoundError:  # Al no encontrar el archivo.
    alerta = '''No se logró encontar el archivo "datos.txt" en la ruta por defecto.',
            Tenga en cuenta que debe estar en la misma carpeta que este programa (archivo ".py")'''
    pretty_print("RED", alerta)
except Exception as excep:
    exception = ' Ocurrió la siguiente excepción: ', type(excep)
    pretty_print("RED", exception)


cod_productos = codigos_sin_repetir(ventas)
sup = diccionario_especial(ventas, cod_productos)

# 1. Imprimir por pantalla los encabezados del archivo y debajo de estos, los datos
# correspondientes a cada registro.

print("\x1b[2J\x1b[H")

pretty_tabla(ventas, 20, " Hola que hace")
siguiente()

# 2. Imprimir los id_producto (código del producto) sin repetir ninguno.

print("Los código del producto son", ", ".join(
    elemento for elemento in cod_productos))
siguiente()

# 3. Imprimir por id_producto el número de ventas.

dic_1 = diccionario_especifico(sup, "número_de_ventas")
pretty_tabla(dic_1, 6, "holi")
siguiente()

# 4. Imprimir por id_producto el valor total vendido

dic_2 = diccionario_especifico(sup, "valor_total")

total = 0
for valor in dic_2["valor_total"]:
    total += valor

separadorcito = separador_horizontal(15)
separadorcito = pretty_print("BLUE", separadorcito[:-1])

total_1 = (separadorcito, "Total")
total_2 = (separadorcito, total)
dic_2['id_producto'].extend(total_1)
dic_2['valor_total'].extend(total_2)

pretty_tabla(dic_2, 8, "holi")

siguiente()


# 5. Imprimir el total de ventas

pretty_tabla(sup, 6, "holi")

siguiente("salir")
