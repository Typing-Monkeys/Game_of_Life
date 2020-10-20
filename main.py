import sys
import numpy as np
import random

''' esempio di stampa della matrice
|   |   |   |
| x | x |   |
|   | x |   |
'''


matrix = None
dimension = 10
amount = 25


def init_matrix():    # popola la matrice al primo avvio
    return np.zeros((dimension, dimension))


def print_matrix(matrix: list):
    for i in matrix:
        for j in i:
            print(
                "| ",
                " " if j == 0. else "x",
                " ",
                end="")

        print("|")


def random_spawn(matrix: np.array, amount: int):
    exit_number = 0
    while exit_number < amount:
        i = random.randint(0, dimension - 1)
        j = random.randint(0, dimension - 1)

        if matrix[i][j] == 0.:
            matrix[i][j] = 1.
            exit_number += 1


def evolve(matrix: np.array):
    pass


def main():
    global matrix
    matrix = init_matrix()
    print_matrix(matrix)

    print("\n", "-"*59, "\n")

    random_spawn(matrix, amount)
    print_matrix(matrix)


if __name__ == "__main__":
    main()
