import os
import numpy as np
import random
from Entity import Entity
from time import sleep

''' esempio di stampa della matrice
|   |   |   |
| x | x |   |
|   | x |   |
'''


dimension = 10  # dimenzione della matrice
amount = 25     # numero di celle vive da spawnare


def init_matrix():    # popola la matrice al primo avvio
    ## -- Migliorare con un Inline for -- ##

    # crea un array con tutti gli elementi che poi verrà ridimenzionato
    # a creare una matrice
    tmp = []
    for _ in range(dimension*dimension):
        tmp.append(Entity())

    return np.array(tmp).reshape((dimension, dimension))


def print_matrix(matrix: list):  # stampa la matrice in modo leggibile
    print("\n", "-"*59, "\n")
    for i in matrix:
        for j in i:
            print(
                "| ",
                j,
                " ",
                end="")

        print("|")

    print("\n", "-"*59, "\n")


def random_spawn(matrix: np.array, amount: int):
    exit_number = 0
    while exit_number < amount:
        # scegli due indici in modo casuale
        i = random.randint(0, dimension - 1)
        j = random.randint(0, dimension - 1)

        # se la cella scelta è morta la porta in vita
        if (matrix[i][j].alive) is False:
            matrix[i][j].set_alive()
            exit_number += 1


def update_entity_neigh(matrix: np.array):
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

    # controlla ogni cella della matrice
    # e ne aggiorna il numero di vicini vivi
    for i in range(dimension):
        for j in range(dimension):
            # prende i vicini della cella
            neght = get_neigh(i, j)

            # controlla se i vicini sono vivi
            for x, y in neght:
                if matrix[x][y].alive is True:
                    matrix[i][j].neighbour_alive += 1


def evolve(matrix: np.array):
    tmp = init_matrix()

    for i in range(dimension):
        for j in range(dimension):
            if matrix[i][j].neighbour_alive == 2 and matrix[i][j].alive:
                tmp[i][j].set_alive()
            if matrix[i][j].neighbour_alive == 3:
                tmp[i][j].set_alive()

    return tmp


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # inizializza la matrice di Entity
    matrix = init_matrix()

    # spona celle vive a caso
    random_spawn(matrix, amount)

    while True:
        clear()
        update_entity_neigh(matrix)

        print_matrix(matrix)

        matrix = evolve(matrix)

        sleep(0.5)


if __name__ == "__main__":
    main()
