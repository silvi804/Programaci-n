""" Abrir el arhivo de texto """
C = 0

with open("datos.txt", encoding='utf8') as archivo:
    lineas = (archivo.readlines()).split(",")
    # print(lineas)
    # lineas.strip("\n")
    # c = 1
    # for linea in lineas:
    #     x = lineas[c]
    for linea in lineas:
        elementos = archivo.readline()
        # print(linea)
        # formato = "{cada_palabra:>15}"
        # " elif
        print(elementos)
    # x = len(lineas)
    # print(x)
        # for cada_palabra in elementos:
        # cada_palabra = elementos[C]
        # if C == 0:
        #     cada_palabra.strip()
        #     print(f"{cada_palabra:>10}", end=" ")
        # if C == 1:
        #     print(f"{cada_palabra:>15}", end=" ")
        # if C == 2:
        #     print(f"{cada_palabra:^15}", end=" ")
        # if C == 3:
        #     print(f"{cada_palabra:^15}", end=" ")
        # if C == 4:
        #     print(f"{cada_palabra:>15}", end=" ")
        # if C == 5:
        #     print(f"{cada_palabra:<15}", end=" ")
        # print(cada_palabra)
        # print(f"{cada_palabra:^15}", end="")
        # C += 1
