''' A continuación la información del equipo 6
    Nombres y Apellidos             Documento   Correo
    Luis David Garzón Morales       1034576806  lgarzonmo@unal.edu.co
    Silvana Suarez Carvajal         1027525528  sisuarezc@unal.edu.co
    Jorge Sebastián Otálora Bernal  1031648550  jotalorab@unal.edu.co
    Yefran David Cespedes Cortes    1123433214  ycespedes@unal.edu.co
    Sergio Nicolás Correa Escobar   1014739037  secorreae@unal.edu.co
'''
class Color:
    Blink  = '\033[5m'   #blink
    Blue   = '\033[34m'  #azul
    Bold   = '\033[1m'   #negrilla 
    Cyan   = '\033[36m'  #cyan
    Green  = '\033[32m'  #verde
    Italy  = '\033[3m'   #itálica
    Purple = '\033[35m'  #púrpura
    Red    = '\033[31m'  #rojo
    Reset  = '\033[0m'   #reset
    Subray = '\033[4m'   #subrayar
    Yellow = '\033[33m'  #amarillo
    White  = '\033[37m'  #blanco
from subprocess import call
call('cls',shell=True) # Limpia la pantalla
print(Color.Green)
print("""Este programa está hecho para decirle que día de la semana es acorde a la fecha que ingresó.
Este código calculará cualquier fecha a partir del 15/10/1582 (acorde al calendario Gregoriano), hasta el siglo 38
    """) 

dias_de_meses={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
semana= {1:"Lunes",2:"Martes",3:"Miércoles",4:"Jueves",5:"Viernes",6:"Sábado",0:"Domingo"} #D
siglos={}
for i in range(15,39):
    e=i-12
    if (e)%4==0: 
        j=6
    elif (e)%4==1:
        j=4
    elif (e)%4==2: 
        j=2
    elif (e)%4==3: 
        j=0
    siglos.update({str(i):j})#ks


def dia_de_la_semana(dia,mes,año):
    x=slice(2)
    y=slice(2,4)
    dia=int(dia)
    año_de_siglo=int(año[y])#A
    siglo=año[x]
    siglo_n=int(siglos[siglo])
    año=int(año)
    siglo=int(siglo)
    cont=True
    mes=int(mes)
    division=(año_de_siglo-(año_de_siglo%4))/4
    outdate = "La fecha no está en el calendario Gregoriano."
    if año<1582:
        print(Color.Yellow)
        print(outdate)
        cont=False
    elif año==1582:
        if mes<10:
            print(Color.Yellow)
            print(outdate)
            cont=False
        elif mes==10:
            if dia<15:
                print(Color.Yellow)
                print(outdate)
                cont=False
                
    if mes not in range(1,13):
            print(Color.Red)
            print("Los meses del año se numeran del 1 al 12, intente de nuevo.")      
    elif dia not in range(1,((dias_de_meses[mes])+1)):
            print(Color.Red)
            print(f"El diá {dia} no existe en el mes {mes}.")
    else:
        mes_a=int(meses[mes])
        if año%4==0 and año%100!=0 or año%400==0:
            dia_de_la_semana=((dia+mes_a+año_de_siglo+division+siglo_n)%7)
        else:   
            if dia==29 and mes==2:
                print(Color.Red)
                print(f"El diá {dia} no existe en el mes {mes} del año {año}.")
                pass
            else:
                dia_de_la_semana=((dia+mes_a+año_de_siglo+division+siglo_n)%7)
        if cont:
            print(Color.Cyan)
            print(f'La fecha corresponde al día: {semana[dia_de_la_semana]}')       

ban = True
while ban:
    print(Color.White)
    try:
        meses={1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}
        fecha=input("A continuación ingrese una fecha de la forma dd/mm/aaaa <Enter = Salir>.\n")
        if fecha== '': ban=False
        if ban:
            dia,mes,año=[i for i in fecha.split('/')]
            if int(año)%4==0 and int(año)%100!=0 or int(año)%400==0:
                meses.update({1:6,2:2})
            dia_de_la_semana(dia,mes,año)
    except:
        print(Color.Red)
        print("La fecha que ingresó no es válida y/o no sigue la estructura de dd/mm/aaaa, intente de nuevo.")