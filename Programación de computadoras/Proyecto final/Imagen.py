import numpy as np
import requests  # pip install requests
import PIL
from PIL import Image
from io import BytesIO
import turtle as tt
url = 'https://img1.freepng.es/20180613/sey/kisspng-old-english-latin-alphabet-letter-english-alphabet-gothic-alphabet-5b21817b4e0120.4788076515289224913195.jpg'

respuesta = requests.get(url)

imagen = Image.open(BytesIO(respuesta.content))

imagen_arreglo = np.asarray(imagen)


def siguiente(array, escala):
    tt.up()
    tt.forward(3*escala)
    tt.setheading(90)
    tt.forward((len(array))*escala)
    tt.down()


def dibujar(array, escala):
    tt.pensize(escala)
    i = 0
    while i < len(array):
        a = 0
        bla = 1
        obla = 1
        for a, valor in enumerate(array[i]):
            if i % 2 == 0:
                if obla == 1:
                    tt.up()
                    tt.setheading(270)
                    tt.forward(escala)
                    tt.setheading(0)
                    tt.down()
                    obla = 0
                n = array[i][a]
                if n == 0:
                    tt.up()
                    tt.forward(escala)
                    tt.down()
                elif n == 255:
                    tt.forward(escala)
            elif i % 2 == 1:
                if bla == 1:
                    tt.up()
                    tt.setheading(270)
                    tt.forward(escala)
                    tt.setheading(180)
                    tt.down()
                    bla = 0
                n = array[i][-(a+1)]
                if n == 0:
                    tt.up()
                    tt.forward(escala)
                    tt.down()
                elif n == 255:
                    tt.forward(escala)
            a += 1
        i += 1


tt.setup(640, 480, -100, 0)  # hay que revisar setup
tt.color('#5c005a', '#a865a7')
tt.up()
tt.goto(-200, 0)
tt.down()

tt.tracer(0, 0)
dibujar(imagen_arreglo, 1)

tt.done()
