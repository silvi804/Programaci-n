'''BLACK.
    RED.
    GREEN.
    YELLOW.
    BLUE.
    MAGENTA.
    CYAN.
    WHITE.'''
    
from subprocess import call
from colorama import Fore
from time import sleep
while True:
    call('cls',shell=True) # Limpia la pantalla
    print(Fore.MAGENTA)
    print('='*20,' Palíndromo','='*20)
    print(Fore.RESET)
    palabra= input("Ingrese una palabra")
    if palabra == '': 
        break
    inverso= list(reversed(palabra))
    print(inverso)
    if inverso==list(palabra):
        print(Fore.CYAN)
        print("Es un palíndormo")
        sleep(5)
    else:
        print(Fore.BLUE)
        print("No es un palíndromo")
        sleep(5)
    