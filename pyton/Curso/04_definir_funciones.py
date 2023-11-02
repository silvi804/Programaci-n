def hola(nombre, apellido="Feliz"):
    # Cuándo no se le pasa un argumento usa el parámetro por defecto
    t = f"¿Cómo estás {nombre} {apellido} ?"
    print(t)


hola("Nicolas", "Ramirez")
hola("chanchito")

# Argumentos nombrados
hola(apellido="Suarez", nombre="Silvana")


def suma(*numeros):  # Iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(1, 2, 3, 4, 5, 6, 7)

# keyword arguments


def get_product(**datos):
    print(datos["id"], datos["name"])
    print(datos)


get_product(id=89,
            name="iohone")

# Return


def resta(a, b):
    resultado = a-b
    return resultado  # return me permite trabajar con el valor fuera de la función


c = resta(5, 2)
d = resta(c, 2)
print(d)
