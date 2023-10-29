
nombre_jugador = input("Por favor, ingresa tu nombre: ")

print(f"Bienvenido, al laberinto {nombre_jugador}!")

import readchar

while True:
   
    key = readchar.readkey()
    
    print(f'Carácter leído: {key}')
    
    if key == '\x1b[A':
        break

print('Programa terminado')