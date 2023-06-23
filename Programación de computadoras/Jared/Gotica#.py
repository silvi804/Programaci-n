import timeit
from skimage import io  # pip install scikit-image
import turtle
from GTextGenerator import *
# Adicional a la anterior versión, buscando hacerlo más rápido, se intentó que se pudiera imprimir la imagen con más tortugas, sin embargo la combinación de líneas
# impresión desde x y y resulta en tiempo peores que el uso de una sola tortuga y se pierde información del dibujo, por lo que se determino que lo mas optimo suele
# ser imprimir la imagen por el ancho o por largo en su total. Se imprime por el que sea mas largo, osea entre el largo y ancho, esto resulta en los mejores tiempos

# Tambien ahora se pueden imprimir imagenes a color osea de 3 canales, y a color trasparentes osea de 4 canales, el resto se imprime en negro

# Y junto a los programas GTextGenrator y GfontGenerator, se puede imprimir cualquier fuente especificando  que se quiere imprimir, poniendo el nombre de la imagen
# que contiene la fuente, y las letras que contiene esta fuente, en los documentos de estos se especifica su funcionamiento

start = timeit.default_timer()
image = GTextGenerator('Jared Ramirez', 'Font1.png',
                       "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!`$%?& \"()-")
# image = io.imread("Berserk.png")/255.0  #Usar este codigo para la prueba a color
try:
    ancho, largo, channels = image.shape
except:
    ancho, largo = len(image), len(image[0])

if ancho > largo:
    threatsY = ancho
    threatsX = 1
else:
    threatsY = 1
    threatsX = largo
turtles = []


def OnCreate():
    turtle.setup(1920, 1080, 0, 0)
    turtle.tracer(False)
    for i in range(threatsY):
        turtlesX = []
        for x in range(threatsX):
            turtlesX.append(turtle.Turtle())
            turtlesX[x].pendown()
        turtles.append(turtlesX)


try:
    if channels == 4:
        def pen(threatsY, treatY, threatsX, treatX):
            ny = (ancho//threatsY)*treatY
            nx = (largo//threatsX)*treatX
            if (image[y+(ny)][x+nx][channels-1] > 0):
                turtles[treatY][treatX].penup()
                turtles[treatY][treatX].setposition(
                    x-(largo//2)+(nx), -y-(ny)+(ancho//2))
                turtles[treatY][treatX].pencolor(
                    image[y+(ny)][x+(nx)][0], image[y+(ny)][x+(nx)][1], image[y+(ny)][x+(nx)][2])
                turtles[treatY][treatX].pendown()
                turtles[treatY][treatX].forward(0.5)
            else:
                turtles[treatY][treatX].penup()
    elif channels == 3:
        def pen(threatsY, treatY, threatsX, treatX):
            ny = (ancho//threatsY)*treatY
            nx = (largo//threatsX)*treatX
            if ((image[y+(ny)][x+nx][0]+image[y+(ny)][x+nx][1]+image[y+(ny)][x+nx][2]) != 3):
                turtles[treatY][treatX].penup()
                turtles[treatY][treatX].setposition(
                    x-(largo//2)+(nx), -y-(ny)+(ancho//2))
                turtles[treatY][treatX].pencolor(
                    image[y+(ny)][x+(nx)][0], image[y+(ny)][x+(nx)][1], image[y+(ny)][x+(nx)][2])
                turtles[treatY][treatX].pendown()
                turtles[treatY][treatX].forward(0.5)
            else:
                turtles[treatY][treatX].penup()
except:
    def pen(threatsY, treatY, threatsX, treatX):
        ny = (ancho//threatsY)*treatY
        nx = (largo//threatsX)*treatX
        if (any(image[y+(ny)][x+nx]) > 0):
            turtles[treatY][treatX].penup()
            turtles[treatY][treatX].setposition(
                x-(largo//2)+(nx), -y-(ny)+(ancho//2))
            turtles[treatY][treatX].pendown()
            turtles[treatY][treatX].forward(0.5)
        else:
            turtles[treatY][treatX].penup()


OnCreate()
for y in range(ancho//threatsY):
    for x in range(largo//threatsX):
        # turtle.tracer(False)
        for treatY in range(threatsY):
            for treatX in range(threatsX):
                pen(threatsY, treatY, threatsX, treatX)
        # turtle.tracer(True)
end = timeit.default_timer()
turtle.done()

print(f"Tiempo: {end - start}")
