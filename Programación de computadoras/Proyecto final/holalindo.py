from turtle import *

setup(1920, 1080, 0, 0)


def cora(size):
    penup()
    right(90)
    forward(100*size)
    left(90)
    pendown()
    # -------
    color('black', 'red')
    begin_fill()
    left(45)
    forward(100*size)
    circle(50*size, 180)
    right(90)
    circle(50*size, 180)
    end_fill()
    forward(100*size)


def mas():
    left(135)
    penup()
    forward(75)
    pendown()
    pensize(20)
    forward(87.5)
    for i in range(0, 4):
        left(90)
        forward(87.5)
        forward(-87.5)


def s():
    penup()
    forward(250)
    left(90)
    forward(300)
    left(90)
    forward(150)
    right(90)
    # ----
    pensize(10)
    begin_fill()
    pendown()

    x = 25
    r = 180

    # s
    circle(3*x, 180)
    circle(-x, r)
    forward(1.5*x)
    circle(x, r)

    forward(1.5*x)

    circle(3*x, 180)
    circle(-x, r)
    forward(2*x)
    circle(x, r)
    forward(2*x)

    end_fill()


cora(2)
mas()
s()
penup()
right(90)
goto(600, -20)
pendown()
s()
done()
