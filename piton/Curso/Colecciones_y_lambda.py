""" 
Esto es una Tupla
Es más rápida pero es inmutable
Tiene índices """

# lenguajes = ("Python", "Java", "C", "C++")
# print(lenguajes[0])
# print(lenguajes)
# print(*lenguajes)


""" Esto es un Diccionario """

# elmundo = {"Python": 1991, "C": 1972, "Java": 1996}
# print(elmundo["Python"])
# print(*elmundo)
# print(elmundo.items())
# print(elmundo.values())

""" 
Conjuntos
Los elementos repetidos se eliminan
no tienden orden
 """
# conjunto_1 = set('6546')
# print(conjunto_1)

# conjunto_1.add('11')
# print(conjunto_1)

# conjunto_1.remove('11') #discard
# print(conjunto_1)

# conjunto_2 = {'1','5','2'}
# print(conjunto_2)

# print('conjunto_1  & conjunto_2: ',conjunto_1 & conjunto_2)

# print('conjunto_1 intersenction(conjunto_2): ', conjunto_1.intersection(conjunto_2))
# print('conjunto_1.union(conjunto_2): ',conjunto_1.union(conjunto_2))

# conjunto_3 = set('Todos queremos')
# print(conjunto_3)

# conjunto_4 = set({1,2,3})
# print(conjunto_4)

# conjunto_5 = set(range(1,7)) #no es aleatorio porque el rango es un iterador
# print(conjunto_5)

# print(5 in conjunto_1)  #si existe en el conjunto: True- False
# In funciona para todas las colecciones

# c = {1, 3, 2, 9, 3, 1,2,9}
# print(c)    #{1, 2, 3, 9}

# unicos = set([3, 5, 6, 1, 5])
# print(unicos)    # {1, 3, 5, 6}


""" anónimas o lambda   
lambda argumentos: expresión
no es necesario proporcionar un nombre
Las funciones Lambda pueden tener cualquier número de argumentos, pero solo una expresión. """


# doble = lambda x: x * 2
# print(doble(7))

# lambda_func = lambda x: True if x**2 >= 10 else False
# lambda_func(3) # Retorna False
# lambda_func(4) # Retorna True


# mi_dicc = {"A": 1, "B": 2, "C": 3}
# print(sorted(mi_dicc)) # Retorna ['C', 'A', 'B']
# print(sorted(mi_dicc, key=lambda x: mi_dicc[x]%3))

""" filter crea una lista de elementos si usados en la llamada a una función devuelven True. 
Es decir, filtra los elementos de una lista usando un determinado criterio. 
filter(function, iterable) """

""" Programa para filtrar los elementos pares de la lista """

# lista = [2, 5, 4, 6, 8, 10, 3]
# nueva_lista = list(filter(lambda x: (x%2 == 0) , lista))
# print(nueva_lista)


""" Programa para filtrar los elementos menores a 0 """

# lista = range(-3, 5)
# menor_cero = list(filter(lambda x: x < 0, lista))
# print(menor_cero)

""" Podemos pasar None como el primer argumento para que filter() tenga el filtro iterador devuelto de cualquier valor que Python considere falso
 """
# aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
# filtered_tanks = list(filter(None, aquarium_tanks))
# print(filtered_tanks)


""" El uso de map aplica una determinada función a todos los elementos de una entrada o lista.
forma: map(funcion_a_aplicar, iterable) """


# lista = range(-3, 5)
# nueva_lista = list(map(lambda x: x * 2 , lista))
# print(nueva_lista)

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]

# print(list( map(lambda x,y : x*y, a,b) ))

# según el man python soporta programación orientada a objetos, procedural o interativa, o funcional
