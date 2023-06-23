from skimage import io
# Este programa en esencia descompone una imagen, en imágenes más pequeñas que son puestas en un diccionario
# Para que este programa funcione la imagen tiene que cumplir las especificaciones de ser un png transparente, que las letras están por filas, y dentro de las filas
# que las letras no estén pegadas, de lo contrario no funcionará, sin embargo es fácil encontrar en internet imágenes de fuentes con tales especificaciones


def GfontGenerator(image, contenido):
    image = io.imread(image)/255.0
    ancho, largo, channels = image.shape
    fila = []
    xS = []
    font = {}
    empty = [0, 0, 0, 0]

    def sortInOne(toSort):  # Este bloque de código permite crear variables que contengan donde empieza y termina el contenido de algo
        sorted = []
        for i in range(len(toSort)):
            if i == 1:
                sorted.append(toSort[0])  # pone el primer elemento
            elif toSort[i-1] != (toSort[i-2]+1):
                # pone los dos elementos que no estan separados por 1, osea que no son continuos
                sorted.append(toSort[i-2])
                sorted.append(toSort[i-1])
        sorted.append(toSort[len(toSort)-1])  # pone el ultimo elemento
        return sorted

    for y in range(ancho):  # Determina en y todas las filas donde hay contenido
        for x in range(largo):
            if (any(image[y][x] > 0)):
                fila.append(y)
                break

    # Se clasifica para que solo queden donde empiezan y terminan las filas
    yS = sortInOne(fila)

    for i in range(len(yS)//2):  # Determina fila por fila, donde hay contenido
        fila = []
        for x in range(largo):
            for y in range(yS[0+i*2], yS[1+i*2]):
                if (any(image[y][x] > 0)):
                    fila.append(x)
                    break
        # Se clasifica el contenido fila por fila, elemento por elemento, donde empieza y termina el contenido
        xS.append(sortInOne(fila))

    # --------------------------------------------------
    # Con las coordenadas de comienzo y fin en y y x, se toma el contenido de estos rangos y se pone en la fuente
    for a in range(len(yS)//2):

        for e in range(len(xS[a])//2):
            letter = []
            for y in range(yS[0+a*2], yS[1+a*2]+1):
                letline = []
                for x in range((xS[a][0+e*2]), (xS[a][1+e*2])+1):
                    letline.append(image[y][x])
                letter.append(letline)
            font.update({contenido[len(font)]: letter})

    emptyespace = []
    # Para todas las fuentes se ayade el ' ' con el mismo largo y ancho que la primera letra que contenga la fuente
    for b in range(len(font[contenido[0]])):
        emptyline = []
        for c in range(len(font[contenido[0]][0])):
            emptyline.append(empty)
        emptyespace.append(emptyline)
    font.update({' ': emptyespace})
    return font
