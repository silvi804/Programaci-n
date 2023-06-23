print("Bienvenido, a continuación podrá transformar un número en base 10 a base 2 ")
while True:
    try:
        i = int(input("A continuación ingrese su número en forma decimal: "))
        base = int(input("¿A que base lo quiere transformar?"))
        contador = -1
        lista = []
        lista1 = []
        if i < 0:
            lista1.append("-")
        while abs(i) >= base:
            d = i % base
            lista.append(d)
            e = (abs(i)-d)/base
            i = e
        if e != 0:
            lista1.append(int(e))

        for a in range(len(lista)):
            c = lista[contador]
            lista1.append(int(c))
            contador -= 1

        print(*lista1)
    except:
        print(" No se puede procesar el valor que ingresó")
