# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from subprocess import call
from color import Color

call('cls', shell=True)  # Limpia la pantalla


''' Impresión de encabezados '''

# imprime ===== cuatro veces
# print('{0} {0} {0} {0}'.format('=' * 10))
# print('=' * 10,'=' * 10,'=' * 10,'=' * 10)
# print(f"{'=' * 10} {'=' * 10} {'=' * 10} {'=' * 10}") #forma moderna
#  #los corchetes permiten traer una variable u operación

""" para acortarlo """
# h = '=' * 10
# print(f'{h} {h} {h} {h}')


''' :< a la iquierda, :> a la derecha, := muestra el signo, :^ centrado '''
# datos = range(1,102,20) #1 21 41 61 81 101
# for i, dato in enumerate(datos): #i contiene el numerado de los datos

#   print('{0:<10} {1:>10} {2:=10} {3:^10}'.format(dato, dato, dato, dato))
# {0:<10} el 0 dice que posición tomar del format y el 10 cuantos espacios

#    print(f'{dato:<10} {dato:>10} {dato:=10} {dato:^10}')
# print('{0} {0} {0} {0}'.format('=' * 10)) #imprime ===== al final de los datos


''' Otro ejemplo de formato '''
# datos = range(500,601,20)
# print('{0}'.format('=' * 7))
# for i in datos:
#   print('{0:^7}'.format(i))
#   print(f'{i:^7}')

''' Color y otra forma de dejar a la derecha a la izquierda o al centro '''

# txt = 'Este es el texto formateado'
# txt = r'\n Este es el texto formateado' #Toma \n como parte del texto
# print(f'El texto tiene {len(txt)} caracteres\n')
# print(Color.GREEN,'\nForma 1 para texto',Color.RESET)
# print(txt.ljust(40,'.'))
# print(txt.rjust(40,'.'))
# print(txt.center(40,'.'))
# print()

''' Otra forma de lograr lo mismo'''
# print(Color.GREEN,'\nForma 2 para texto',Color.RESET)
# print(format(txt,'.<40'))
# print(format(txt,'.>40'))
# print(format(txt,'.^40'))
# print()

''' Con números'''
# numero = 129.3467
# print(Color.GREEN,'\nFormato para alinear números',Color.RESET)
# print(format(numero,'.<40')) #format lo transforma internamente en string
# print(format(numero,'.>40'))
# print(format(numero,'.^40'))
