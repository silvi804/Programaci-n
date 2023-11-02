""" instrucciones sobre archivos """

# x: crear archivo
# w: crea o sobre escribe
# a: adiciona datos al final del archivo
# r: archivo de lectura

""" operacione sobre archivos: """

# open()
# close()

""" read() """
# f.read(size) 
# sólo retorna cadenas
# size es un argumento numérico opcional
# se omite size o es negativo, el contenido entero del archivo será leído y retornado

""" readline() """
# f.readline() 
# lee una sola linea del archivo; el carácter de fin de linea (\n) se deja al final de la cadena
# para leer todas las líneas
#list(f)
#f.readlines()
#for line in f:
#   print(line, end='')

""" write() """
# f.write(cadena) 
# escribe el contenido de la cadena al archivo, retornando la cantidad de caracteres escritos.

# seek 


"""
Apuntadores: estructura de memoria que contiene toda la información pertinente
La manera en que obtengo información 

with:
Estructura de bloques de contexto
Se utiliza para no dar la instrucción de close
"""

""" Ejemplos """

# f = open("archivo.txt","r", encoding="utf-8")
# texto = f.read()

# with open("archivo.txt") as f: #buena práctica
#     texto= f.read()

""" 
Json:
data interchange format, interoperabilidad
Son rápidos de transmitir, y es nativo para los analizadores de java_script
XML si cuenta con extensibilidad, este no
Solo soporta datos comunes
No tiene ningún tipo de protección
"""
import json
# x = [1, 'simple', 'list']
# print( json.dumps(x)) #muestra su representación json
# json.dump(x, f)
# x = json.load(f)

""" Transformar de python a json """
# with open("datos.json", "w") as file:
#     json.dump(registro, file, ensure_ascii=False, indent=4)
    
""" Transformar de json a python """
with open("datos.json", "r") as file:
    registro= json.dump(file)
