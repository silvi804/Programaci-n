from GfontGenerator import *
# Este programa toma las imágenes especificadas de el diccionario font, y las une en el orden especificado, para componer una sola imagen


def GTextGenerator(text, imagefont, contentfont):
    font = GfontGenerator(imagefont, contentfont)
    textline = []
    empty = [0, 0, 0, 0]
    for i in range(len(text)):  # Suma letra por letra a textline
        if i == 0:
            for a in range(len(font[text[i]])):
                textline.append(font[text[i]][a])
        else:
            while True:
                # Si  la letra es menor en y que la otras imagen, iguala la letra
                if len(textline) < len(font[text[i]]):
                    emptyline = []
                    for c in range(len(textline[0])):
                        emptyline.append(empty)
                    textline.append(emptyline)
                # Si la cadena de texto es menor en y que la letra las iguala
                elif len(textline) > len(font[text[i]]):
                    emptyline = []
                    for c in range(len(font[text[i]][0])):
                        emptyline.append(empty)
                    font[text[i]].append(emptyline)
                else:  # Siendo que ya son iguales las imagenes, las suma fila por fila
                    for b in range(len(textline)):
                        textline[b] = textline[b] + font[text[i]][b]
                    break
    return textline
