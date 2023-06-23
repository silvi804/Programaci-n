""" Abrir el archivo de texto """
from subprocess import call


diccionario = {}
datos_id = {}

call('cls', shell=True)


def espera_input():
    input("Presiona Enter para continuar...")
    call('cls', shell=True)


with open("datos.txt", encoding='utf8') as archivo:
    cantidad_lineas = len(archivo.readlines())

    archivo.seek(0)
    encabezado = (archivo.readline()).split(",")

    for key in encabezado:
        diccionario[key] = []

    for linea in archivo:
        linea_individual = linea.split(",")
        # linea_individual = (archivo.readline()).split(",")
        # print(linea)
        for key in encabezado:
            for i, valor in enumerate(linea_individual):

                if encabezado.index(key) == i:
                    diccionario[key].append(valor)
                else:
                    pass


# 1.	Imprimir por pantalla los encabezados del archivo
# y debajo de estos, los datos correspondientes a cada registro.

# Imprimir los encabezados
for key in encabezado:
    print("{:<20}".format(key), end="")
print()

# Imprimir cada fila de datos
for i in range(cantidad_lineas-1):
    print()
    for key in encabezado:
        print("{:<20}".format(diccionario[key][i]), end="")

espera_input()

# 2. Imprimir los id_producto (código del producto) sin repetir ninguno.

los_id_producto = sorted(set(diccionario["id_producto"]))

print("Los código del producto son", ", ".join(
    elemento for elemento in los_id_producto))

""" Se crea un diccionario con cada id_producto, la cantidad vendida y el numero de ventas"""

codigo_producto = diccionario["id_producto"]
datos_id["id_producto"] = ["cantidad", "venta"]

for numero in los_id_producto:
    indice = codigo_producto.index(numero)
    precio_individual = diccionario["precio_unitario"][indice]

    datos_id[numero] = [0]

    for i, llave_producto in enumerate(codigo_producto):  # es la larga
        if llave_producto == numero:
            n_ventas = diccionario["cantidad"][i]
            datos_id[numero][0] = (datos_id[numero][0]) + int(n_ventas)

    cantidad = (float(precio_individual))*(datos_id[numero][0])
    datos_id[numero].append(cantidad)

espera_input()

# 3. Imprimir por id_producto el número de ventas.
# 4. Imprimir por id_producto el valor total vendido


for clave, valor in datos_id.items():
    print(f"{clave:<20}", end=" ")
    for elemento in valor:
        print(f"{elemento:<20}", end=" ")

    print("\n")

espera_input()

# for llaves in datos_id:


# 5. Imprimir el total de ventas
