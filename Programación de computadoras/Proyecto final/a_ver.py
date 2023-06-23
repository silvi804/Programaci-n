from turtle import *



size = (20, 30)


setup(640, 480, -100, 0)
color('#5c005a', '#a865a7')
x = 25
i = 0
pensize(x)

array = [[1, 1, 0],
         [1, 0, 0],
         [1, 0, 0]]


while i < len(array):
    a = 0
    bla = 1
    obla = 1
    for a, valor in enumerate(array[i]):
        if i % 2 == 0:
            if obla == 1:
                up()
                setheading(270)
                forward(x)
                setheading(0)
                down()
                obla = 0
            n = array[i][a]
            if n == 0:
                up()
                forward(x)
                down()
                # print("oa")
            elif n == 1:
                forward(x)
                # print("ash")
        elif i % 2 == 1:
            if bla == 1:
                up()
                setheading(270)
                forward(x)
                setheading(180)
                down()
                bla = 0
            n = array[i][-(a+1)]
            if n == 0:
                up()
                forward(x)
                down()
                # print("oa")
            elif n == 1:
                forward(x)
                # print("ash")
        a += 1
    i += 1

up()
forward(3*x)
setheading(90)
forward((len(array)-1)*x)
down()
# a = 0
# b = 0
# while a < len(i):
#     if i[a] == 1:
#         forward(1.5*x)
#         a += 1
#         # a += 1
#         if i[a+1] == 1:
#             forward(1.5*x)
#         else:
#             right(90)
#             forward(1.5*x)
#             break
#     else:
#         a += 1

#     b = i[a]

# # s
# circle(3*x, 180)
# circle(-x, r)
# circle(x, r)

# forward(1.5*x)


# circle(3*x, 180)
# circle(-x, r)
# forward(2*x)
# circle(x, r)
# forward(2*x)


# end_fill()

done()
