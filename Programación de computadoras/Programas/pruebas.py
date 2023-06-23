# # diccionario = {
# #     "llave1": [1, 2, 3],
# #     "llave2": ["a", "b", "c"],
# #     "llave3": [True, False, True]
# # }

# # for llave in diccionario:
# #     primer_valor = diccionario[llave][0]
# #     print("El primer valor de la llave", llave, "es", primer_valor)


# diccionario = {"llave1": "valor1", "llave2": "valor2"}

# # Agregar una nueva llave y valor al diccionario
# diccionario["llave3"] = "valor3"

# # Imprimir el diccionario completo para verificar la nueva entrada
# # print(diccionario)


# listas = {}
# for i in range(3):
#     nombre_lista = "lista_" + str(i)
#     listas[nombre_lista] = []

#     for j in range(3):
#         valor = j + 1
#         listas[nombre_lista].append(valor)
# print(listas)

# mi_lista = [1, 2, 3, 4, 5]
# separador = ", "

# print(separador.join(str(elemento) for elemento in mi_lista))

# for i in range(len(diccionario["id_producto"])):
#     for columna in tabla.keys():
#         print("{:<15}".format(diccionario[columna][i]), end="")
#     print()

# diccionario = {'a': 1, 'b': 2, 'c': 3}

# for clave, valor in diccionario.items():
#     print(clave, valor)

# cadena = "ejemplo"
# lista = list(cadena)
# del lista[:2]  # Eliminar los dos primeros caracteres
# del lista[-2:]  # Eliminar los dos últimos caracteres
# cadena_resultante = ''.join(lista)
# print(cadena_resultante)

# dividendo = 20
# divisor = 3
# # realizar la división y guardar el resultado en una variable
# resultado = dividendo / divisor
# # obtener el resto de la división y guardar el resultado en una variable
# parte_decimal = resultado % 10000
# print(parte_decimal)

encabezado = ['Nombre', 'Apellido', 'Edad', 'Ciudad']
formato = ""

for key in encabezado:
    longitud = len(key)+8
    formato += f"{key:^{longitud}}"

formato += "\n"

print(formato)
