import os
import time
import curses
from typing import List, Tuple

nombre_jugador = input("Por favor, ingresa tu nombre: ")

print(f"Bienvenido, al laberinto {nombre_jugador}!")

def mostrar_laberinto(stdscr, laberinto):
    for i, fila in enumerate(laberinto):
        stdscr.addstr(i, 0, ''.join(fila))
    stdscr.refresh()

def main_loop(stdscr, laberinto, inicio, fin):
    px, py = inicio

    while (px, py) != fin:
        laberinto[px][py] = 'P'  # Colocar el jugador en la posición actual
        mostrar_laberinto(stdscr, laberinto)

        # Esperar un breve período de tiempo
        time.sleep(0.3)

        # Calcular la nueva posición tentativa automáticamente
        nueva_px, nueva_py = px, py
        key = stdscr.getch()
        if key == curses.KEY_UP and px > 0:
            nueva_px -= 1
        elif key == curses.KEY_DOWN and px < len(laberinto) - 1:
            nueva_px += 1
        elif key == curses.KEY_LEFT and py > 0:
            nueva_py -= 1
        elif key == curses.KEY_RIGHT and py < len(laberinto[0]) - 1:
            nueva_py += 1

        # Verificar si la nueva posición es válida
        if 0 <= nueva_px < len(laberinto) and 0 <= nueva_py < len(laberinto[0]) and laberinto[nueva_px][nueva_py] != '#':
            # Restaurar la posición anterior solo si la posición actual ha cambiado
            if (nueva_px, nueva_py) != (px, py):
                laberinto[px][py] = '.'
            # Actualizar la posición del jugador
            px, py = nueva_px, nueva_py
        else:
            # Si se encuentra con una pared, salir del bucle
            break

    # Verificar si el jugador llegó al final
    if (px, py) == fin:
        mostrar_laberinto(stdscr, laberinto)
        stdscr.addstr(len(laberinto), 0, "¡Felicidades! Has llegado al final del laberinto.")
        stdscr.refresh()
        stdscr.getch()
    else:
        stdscr.addstr(len(laberinto), 0, "¡Has perdido! Te has encontrado con una pared.")
        stdscr.refresh()
        stdscr.getch()

def empezar_juego(stdscr):
    laberinto_str = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

    laberinto_filas = laberinto_str.split("\n")
    laberinto = [list(fila) for fila in laberinto_filas]

    inicio = (0, 0)
    fin = (len(laberinto) - 1, len(laberinto[0]) - 1)

    main_loop(stdscr, laberinto, inicio, fin)

# Llamar a la función para comenzar el juego
curses.wrapper(empezar_juego)







