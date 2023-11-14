import os
import time
import curses
import random

class Juego:
    def __init__(self, nombre_jugador, laberinto_str):
        self.nombre_jugador = nombre_jugador
        self.laberinto_str = laberinto_str
        self.laberinto_filas = laberinto_str.split("\n")
        self.laberinto = [list(fila) for fila in self.laberinto_filas]
        self.inicio = (0, 0)
        self.fin = (len(self.laberinto) - 1, len(self.laberinto[0]) - 1)

    def mostrar_laberinto(self, stdscr):
        for i, fila in enumerate(self.laberinto):
            stdscr.addstr(i, 0, ''.join(fila))
        stdscr.refresh()

    def main_loop(self, stdscr):
        px, py = self.inicio

        while (px, py) != self.fin:
            self.laberinto[px][py] = 'P'
            self.mostrar_laberinto(stdscr)

            time.sleep(0.3)

            nueva_px, nueva_py = px, py
            key = stdscr.getch()
            if key == curses.KEY_UP and px > 0:
                nueva_px -= 1
            elif key == curses.KEY_DOWN and px < len(self.laberinto) - 1:
                nueva_px += 1
            elif key == curses.KEY_LEFT and py > 0:
                nueva_py -= 1
            elif key == curses.KEY_RIGHT and py < len(self.laberinto[0]) - 1:
                nueva_py += 1

            if 0 <= nueva_px < len(self.laberinto) and 0 <= nueva_py < len(self.laberinto[0]) and self.laberinto[nueva_px][nueva_py] != '#':
                if (nueva_px, nueva_py) != (px, py):
                    self.laberinto[px][py] = '.'
                px, py = nueva_px, nueva_py
            else:
                break

        if (px, py) == self.fin:
            self.mostrar_laberinto(stdscr)
            stdscr.addstr(len(self.laberinto), 0, f'¡Felicidades, {self.nombre_jugador}! Has llegado al final del laberinto.')
            stdscr.refresh()
            stdscr.getch()
        else:
            stdscr.addstr(len(self.laberinto), 0, f'¡{self.nombre_jugador}, has perdido! Te has encontrado con una pared.')
            stdscr.refresh()
            stdscr.getch()

    def empezar_juego(self, stdscr):
        self.main_loop(stdscr)

class JuegoArchivo(Juego):
    def __init__(self, nombre_jugador, path_a_mapas):
        super().__init__(nombre_jugador, self.cargar_mapa_aleatorio(path_a_mapas))

    def cargar_mapa_aleatorio(self, path_a_mapas):
        lista_archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(lista_archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido = archivo.read()

        return contenido.strip()

# Uso del juego con un laberinto fijo
nombre_jugador = input("Por favor, ingresa tu nombre: ")
juego_fijo = Juego(nombre_jugador, """..###################
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
###################..""")

curses.wrapper(juego_fijo.empezar_juego)

# Uso del juego con un laberinto cargado desde un archivo
juego_desde_archivo = JuegoArchivo(nombre_jugador, "directorio_de_mapas")
curses.wrapper(juego_desde_archivo.empezar_juego)

















