'''Proyecto Final'''

# Funciones:


from subprocess import call


def siguiente(proceso):  # Permite mostrar la siguiente "pantalla" con "enter".
    input(f'\n Presione {Color.GREEN}"enter"{Color.RESET} para {proceso}.\n ')
    call('cls', shell=True)
    call('cls', shell=True)


def clasificar(datos):  # Devuelve un diccionario con los datos organizados.
    categorias, datos = {}, datos.read().split('\n')
    encabezado = datos[0].split(',')
    for categoria in encabezado:
        categorias[categoria] = []
    for linea in range(1, len(datos)):
        elementos = datos[linea].split(',')
        for elemento, categoria in enumerate(categorias):
            categorias[categoria].append(elementos[elemento])
    return categorias


def tabla_datos(categorias):  # Imprime la tabla con los datos del archivo.
    # (También se puede hacer más corto con XY, pero se desconfiguraría dependiendo del tamaño de la terminal)
    tamaño, horizontal, vertical = 5, f'{Color.BLUE}={Color.RESET}', f'{Color.BLUE}|{Color.RESET}'
    for categoria in categorias:
        tamaño += len(categoria) + 5
    print(
        ' ' * 5, f'{f"{Color.GREEN}{Color.SUBRAY}Programa de Cálculo de Ventas{Color.RESET}":^{tamaño}}\n')
    print(f'  {Color.BLUE}.', end='')  # (Imprime el inicio de la tabla)
    for categoria in categorias:
        ancho = len(categoria) + 4
        print(f'{horizontal * ancho}{Color.BLUE}.', end='')
    print('')
    print(f'  {vertical}', end='')  # (Imprime el encabezado)
    for categoria in categorias:
        print(f'  {Color.BLUE}{categoria}', end=f'  {vertical}')
    print('')
    print(f'  {vertical}', end='')  # (Imprime la división de la tabla)
    for categoria in categorias:
        ancho = len(categoria) + 4
        print(f'{horizontal * ancho}', end=f'{vertical}')
    print('')
    # (Imprime el contenido)
    for elemento in range(len(categorias['id_producto'])):
        print(f'  {vertical}', end='')
        for categoria in categorias:
            print(
                f'  {categorias[categoria][elemento]:>{len(categoria)}}  ', end=vertical)
        print('')
    print(f'  {Color.BLUE}\'', end='')  # (Imprime el cierre de la tabla)
    for categoria in categorias:
        ancho = len(categoria) + 4
        print(f'{horizontal * ancho}', end=f'{Color.BLUE}\'')
    print(f'{Color.RESET}')


def organizar(lista):  # Devuelve los id_producto organizados.
    # (Es lo mismo que el "sorted (set (id_producto))"... Se puede reemplazar por eso)
    lista_id, indice = [], 0
    verify = True
    while indice in range(len(lista)):
        elemento = lista[indice]
        if elemento not in lista_id:
            if verify:
                lista_id.append(elemento)
                verify = False
                indice += 1
                continue
            indice_id = 0
            while indice_id in range(len(lista_id)):
                if (int(elemento) < int(lista_id[indice_id])):
                    lista_id.insert(indice_id, elemento)
                    break
                if indice_id + 1 not in range(len(lista_id)):
                    lista_id.append(elemento)
                    break
                indice_id += 1
        indice += 1
    return lista_id


# Devuelve un diccionario con los datos (cantidades, precios, etc.) por id_producto.
def info_id(categorias):
    categorias2 = {}
    categorias2['id_producto'], categorias2['número_ventas'] = organizar(
        categorias['id_producto']), []
    categorias2['cantidad_vendida'], categorias2['precio_unitario'], categorias2['valor_total'] = [], [], []
    id_indices = {id: [] for id in categorias2['id_producto']}
    for id in categorias2['id_producto']:
        indice = 0
        for elemento in categorias['id_producto']:
            if elemento == id:
                id_indices[id].append(indice)
            indice += 1
        categorias2['número_ventas'].append(len(id_indices[id]))
        cantidad = 0
        for indi in id_indices[id]:
            cantidad += int(categorias['cantidad'][indi])
        categorias2['cantidad_vendida'].append(cantidad)
        categorias2['precio_unitario'].append(
            categorias['precio_unitario'][id_indices[id][0]])
    for index in range(6):
        categorias2['valor_total'].append(
            categorias2['cantidad_vendida'][index] * float(categorias2['precio_unitario'][index]))
    return categorias2


def tabla_ventas(categorias):  # Imprime la tabla de cantidades y precios.
    tabla_datos(categorias)
    total, horizontal = 0, '='
    for indi in categorias['valor_total']:
        total += indi
    print(
        f'  {Color.BLUE}|{"Total:":^15}{" " * 59}|{Color.RESET}{total:>13}  {Color.BLUE}|')
    print(f'  \'{horizontal * 90}\'')

# Ejecución:


call('cls', shell=True)  # Limpiar la terminal.

try:
    from color import Color
    with open('datos.txt', 'r') as archivo:  # Apertura del archivo.
        datos_dic = clasificar(archivo)
except FileNotFoundError:  # Al no encontrar el archivo.
    print(f'{Color.RED} No se logró encontar el archivo "datos.txt" en la ruta por defecto.',
          '\n Tenga en cuenta que debe estar en la misma carpeta que este programa (archivo ".py").',
          f'\n Si está usando Visual Studio Code, debe encontrarse en la carpeta principal abierta.{Color.RESET}')
except ModuleNotFoundError:  # Al no encontrar el módulo.
    print('\033[31m No se logró encontar el archivo "color.py" en la ruta por defecto.',
          '\n Tenga en cuenta que debe estar en la misma carpeta que este programa (archivo ".py").\033[0m')
# Identificador de otras excepciones posibles (no contempladas).
except Exception as excep:
    print(f'{Color.RED} Ocurrió la siguiente excepción: ',
          type(excep), f'{Color.RESET}')
else:  # (Instrucciones a ejecutar después de haber almacenado los datos)
    tabla_datos(datos_dic)
    siguiente('continuar')
    id_info = info_id(datos_dic)
    tabla_ventas(id_info)
    siguiente('salir')
