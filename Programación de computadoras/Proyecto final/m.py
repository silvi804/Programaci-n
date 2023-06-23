with open('matricita.txt', 'r') as matrices_sin_formato:
    numero_lineas = len(matrices_sin_formato.readlines())
    matrices_sin_formato.seek(0)
    with open('matrices1_formateadas.txt', 'w') as matriz_arreglada:
        for i in range(numero_lineas):
            matriz = matrices_sin_formato.readline().strip('\n')
            lista = []
            for j in matriz:
                lista.append(int(j))
            lista = str(lista)
            matriz_arreglada.write(lista + ',' + '\n')
