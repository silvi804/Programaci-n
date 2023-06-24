print("Bienvenidos a la calculadora \nPara salir escribe Salir\nLas operaciones son suma, multi, div, y resta")
n_1 = 0
while True:
    if not n_1:
        n_1 = input("Número uno ")
        if n_1.lower == "salir":
            break
        n_1 = int(n_1)

    operacion = input("operacion ")
    if operacion.lower == "salir":
        break
    n_2 = input("Número 2")
    if n_2.lower == "salir":
        break
    n_2 = int(n_2)

    if operacion.lower() == "suma":
        n_1 += n_2
    elif operacion.lower() == "multi":
        n_1 *= n_2
    elif operacion.lower() == "div":
        n_1 /= n_2
    elif operacion.lower() == "resta":
        n_1 -= n_2
    else:
        print("Operación no válida")
        break

    print(f"El resultado es {n_1}")
