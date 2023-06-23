from subprocess import call
call('cls', shell=True)  # Limpia la pantalla
print("""Este programa está hecho para decirle que día de la semana es acorde a la fecha que ingresó.
Este código calculará cualquier fecha a partir del 15/10/1582 (acorde al calendario Gregoriano), hasta el siglo 38
    """)
meses = {3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
dias_de_meses = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
semana = {1: "Lunes", 2: "Martes", 3: "Miercoles",
          4: "Jueves", 5: "Viernes", 6: "Sábado", 0: "Domingo"}  # D
siglos = {}
for i in range(15, 38):
    if (i-16) % 4 == 0:
        j = 6
    elif (i-16) % 4 == 1:
        j = 4
    elif (i-16) % 4 == 2:
        j = 2
    elif (i-16) % 4 == 3:
        j = 0

    siglos.update({str(i): j})  # ks


def dia_de_la_semana(dia, mes, año):
    x = slice(2)
    y = slice(2, 4)
    dia = int(dia)
    año_de_siglo = int(año[y])  # A
    siglo = año[x]
    siglo_a = int(siglos[siglo])
    año = int(año)
    mes = int(mes)
    division = (año_de_siglo-(año_de_siglo % 4))/4
    y = True

    if int(siglo) <= 15:
        if año_de_siglo <= 82:
            if (mes == 10 and dia < 15) or mes < 10:
                print("La fecha no está en el calendario Gregoriano")
                y = False
        if int(siglo) > 37:
            print("Este código no contempla más allá del siglo 38")
    while y:
        if dia not in range(1, (dias_de_meses[mes]+1)):
            print(f"El diá {dia} no existe en el mes {mes}")
        elif mes not in range(1, 13):
            print("Los meses del año se numeran del 1 al 12")
        else:
            if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
                meses.update({1: 6, 2: 2})
            else:
                if dia == 29 and mes == 2:
                    pass
                else:
                    meses.update({1: 0, 2: 3})

            mes_a = int(meses[mes])
            dia_de_la_semana = ((dia+mes_a+año_de_siglo+division+siglo_a) % 7)
            print(semana[dia_de_la_semana])
        y = False


while True:
    try:
        fecha = input(
            "A continuación ingrese una fecha de la forma dd/mm/aaaa <Enter = Salir> \n")
        if fecha == '':
            break
        dia, mes, año = [i for i in fecha.split('/')]
        dia_de_la_semana(dia, mes, año)
    except:
        print("La fecha que ingresó no es válida y/o no sigue la estructura de dd/mm/aaaa, intente de nuevo ")
