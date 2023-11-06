import os
import readchar

numero = 0

def print_num():
    os.system('cls' if os.name=='nt' else 'clear')
    print(numero)

print('presione la tecla "n"')

while numero <= 50:
    key = readchar.readkey()

    if key == 'n':
        print_num()
        numero += 1
    else:
        print('presione la tecla n')

print('haz llegado hasta el final')