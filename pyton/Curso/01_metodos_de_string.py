animal = " no jodas"
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.strip().capitalize())  # Se pueden encadenar métodos
print(animal.title())
print(animal.strip())  # Elimina espacios a la izquiera y a la derecha
print(animal.lstrip())  # Lo hace a la iquierda
print(animal.rstrip())  # Lo hace a la derecha
# Devuelve el primer índice en el que está la cadena y un -1 si no lo encuentra
print(animal.find("o"))
print(animal.replace("o", "i"))  # tiene 2 argumentos
