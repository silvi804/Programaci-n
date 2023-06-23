sum = 0
contador= 0
lista=[ ]
print("Bienvenido, este código le otorgará el menor número, el mayor número y el promedio de los datos que ingrese.\nA continuación ingrese la cantidad de números que desee \nAl finalizar digite la palabra fin")
while True:
    try:
        i=input("Ingrese el siguiente número: ")
        if type(float(i))==float:
            contador+= 1
        lista.append(i)
        sum += float(i)
    except:
        if i.lower()=="fin":
            try:
                if len(lista)==1:
                    print("Solo ingreso un número, por lo que no se requiere determinar el menor, el mayor o el promedio, pues los tres corresponden a",lista[0])
                else:
                    print("El menor de sus datos es: ",min(lista))
                    print("El mayor de sus datos es: ",max(lista))
                    print("Y por último el promedio de los datos que ingresó es ",sum/contador)
                    break
            except:
                print("No ingresó ningún valor numérico")
                break
        else:
            print("No se puede operar con tipo de dato que ingresó, inténtelo de nuevo.")
    