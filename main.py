import os
import random
import pygame
import numpy as np
from Entity import Entity
from time import sleep


# variabili per la matrice
dimension   = 120  # dimenzione della matrice
amount      = 4000  # numero di celle vive da spawnare
tempo       = 0.01

# colori per l'interfaccia grafica
cellsize    = 8   # dimensione celle
col_alive   = (255, 255, 215)
col_grid    = (30, 30, 60)
col_background = (10, 10, 40)


# genera una nuova matrice
def init_matrix() -> np.array:
    # crea un array con tutti gli elementi che poi verrà ridimenzionato
    # a creare una matrice
    tmp = []
    for _ in range(dimension*dimension):
        tmp.append(Entity())

    return np.array(tmp).reshape((dimension, dimension))


# stampa la matrice in modo leggibile
def print_matrix(matrix: np.array):
    print("\n", "-"*59, "\n")
    for i in range(dimension):
        for j in range(dimension):
            print(
                "| ",
                matrix[i][j],
                " ",
                end="")

        print("|")

    print("\n", "-"*59, "\n")


# funzione per generare casualmente un set di
# Entity vive iniziale
def random_spawn(matrix: np.array, amount: int):
    exit_number = 0
    while exit_number < amount:
        # scegli due indici in modo casuale
        i = random.randint(0, dimension - 1)
        j = random.randint(0, dimension - 1)

        # se la cella scelta è morta la porta in vita
        if matrix[i][j].alive is False:
            matrix[i][j].set_alive()
            exit_number += 1


# funzione per evolvere la matrice
def evolve(matrix: np.array, surface: pygame.surface) -> np.array:
    # data un determinata cella restituisce le celle vicine
    def get_neigh(x, y):
        # presa da https://stackoverflow.com/questions/1620940/determining-neighbours-of-cell-two-dimensional-list
        # come un ottimo bardipo :+1: ESSENTIAL
        return [
            (x2, y2)
            for x2 in range(x-1, x+2)
                for y2 in range(y-1, y+2)
                    if (-1 < x <= dimension - 1 and
                        -1 < y <= dimension - 1 and
                        (x != x2 or y != y2) and
                        (0 <= x2 <= dimension - 1) and
                        (0 <= y2 <= dimension - 1))
            ]

    # matrice temporanea
    tmp = init_matrix()

    for i in range(dimension):
        for j in range(dimension):
            col = col_background

            # -- aggiorna i vicini della cella attuale -- #
            neight = get_neigh(i, j)

            # controlla se i vicini sono vivi
            for x, y in neight:
                if matrix[x][y].alive is True:
                    matrix[i][j].neighbour_alive += 1
            # -------------------- #

            # evolve la cella attuale
            if matrix[i][j].neighbour_alive == 2 and matrix[i][j].alive:
                tmp[i][j].set_alive()
                col = col_alive
            if matrix[i][j].neighbour_alive == 3:
                tmp[i][j].set_alive()
                col = col_alive

            # stampa graficamente la cella attuale
            pygame.draw.rect(surface, col, (j*cellsize, i*cellsize, cellsize-1, cellsize-1))

    return tmp


# pulisce lo schermo
# il comando cambia in base al OS
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# funzione per mostrare la prima generazione della matrice
def show_first_gen(matrix: np.array, surface: pygame.surface):
    # stampa la griglia della matrice
    surface.fill(col_grid)

    # colora tutte le celle in base al loro stato
    for i in range(dimension):
        for j in range(dimension):
            if matrix[i][j].alive:
                col = col_alive
            else:
                col = col_background

            # stampa la cella corrente
            pygame.draw.rect(surface, col, (j*cellsize, i*cellsize, cellsize-1, cellsize-1))

    # aggiorna la finestra
    pygame.display.update()


def main():
    # inizializza pygame e il display
    pygame.init()
    surface = pygame.display.set_mode((dimension * cellsize, dimension * cellsize))
    pygame.display.set_caption("Typing Monkeys's Game of Life")

    # inizializza la matrice di Entity
    matrix = init_matrix()

    # spona celle vive a caso
    random_spawn(matrix, amount)

    # mostra a video la prima generazione della matrice
    show_first_gen(matrix, surface)

    sleep(tempo)

    # evolve la matrice
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # stampa la griglia della matrice
        surface.fill(col_grid)

        # evolve la matrice
        matrix = evolve(matrix, surface)

        # aggiorna la finestra
        pygame.display.update()

        sleep(tempo)


if __name__ == "__main__":
    main()
