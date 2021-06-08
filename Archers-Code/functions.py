# -*- coding: utf-8 -*-

from random import randint

N = 4  # Dimensiunea tabelului NxN
table = [['-' for x in range(N)] for y in range(N)]  # Blank table
# noinspection PyRedeclaration
pos = [-1 for x in range(N)]  # Archers positions
ok = 0


def hash(name):  # functia hash
    return 1 + (sum(ord(c) for c in name) % 6)


def printTable():  # Afisarea tabelului in fisierul de iesire
    # noinspection PyBroadException
    try:
        f = open('output.txt', 'a')

    except:
        print("EROARE: Nu s-a putut deschide fisierul la iesire")

    else:
        for i in range(N):
            for j in range(N):
                f.write(table[i][j] + ' ')
            f.write('\n')
        f.write('\n')


def searchDFS(index):  # Cautare DFS pentru pozitiile arcasilor
    global ok
    global pos

    if index >= N:
        if check(index):
            printNoWalls()
            printWithWalls()
            ok = 1

    if ok == 0 and index < N:
        for col in range(N):
            pos[index] = col
            searchDFS(index + 1)


def check(index):  # Verificam pozitia arcasului
    for line_i in range(index):
        for line_j in range(line_i + 1, index):
            col_i = pos[line_i]
            col_j = pos[line_j]
            if threatens(line_i, col_i, line_j, col_j):
                return False
    return True


def threatens(line_i, col_i, line_j, col_j):  # Verificam daca este cumva vreun arcas pe aceeasi linie/coloana/diagonala
    if line_i == line_j or col_i == col_j or abs(line_i - line_j) == abs(col_i - col_j):
        return True
    else:
        return False


def randomWall():  # Luam aleatoriu un zid pentru a schimba pozitia arcasului
    wall_l = randint(0, N - 1)
    wall_c = pos[wall_l]

    return wall_l, wall_c


def printNoWalls():  # Afisam tabelul cu arcasii, fara pereti
    for i in range(N):
        table[i][pos[i]] = 'A'

    printTable()


def printWithWalls():  # Afisam tabelul cu arcasii si peretii
    OK1 = 1
    wall_l, wall_c = randomWall()
    table[wall_l][wall_c] = '-'

    if wall_l > 0:
        wall_l -= 1
    else:
        wall_l += 1

    while OK1 == 1:  # Verificam daca arcasul respectiv poate fi pus in acea pozitie
        OK = 1
        for i in range(N):
            if table[i][pos[i]] == 'A':
                if i == wall_l and (pos[i] - 1 == wall_c or pos[i] + 1 == wall_c): OK = 0
                if pos[i] == wall_c and (i - 1 == wall_l or i + 1 == wall_l): OK = 0
                if pos[i] == wall_c and i == wall_l:
                    if i - 1 == wall_l and pos[i] - 1 == wall_c: OK = 0
                    if i - 1 == wall_l and pos[i] + 1 == wall_c: OK = 0
                    if i + 1 == wall_l and pos[i] - 1 == wall_c: OK = 0
                    if i + 1 == wall_l and pos[i] + 1 == wall_c: OK = 0

        if OK == 0:
            if wall_c > 0:
                wall_c -= 1
            elif wall_c == 0:
                wall_c += 1
        else:
            OK1 = 0

    for i in range(N):  # Punem pereti acolo unde sunt arcasi pe aceeasi linie/coloana/diagonala
        if table[i][pos[i]] == 'A':
            if i == wall_l:
                if pos[i] < wall_c:
                    table[i][pos[i] + 1] = 'W'
                elif pos[i] > wall_c:
                    table[i][pos[i] - 1] = 'W'

            if pos[i] == wall_c:
                if i < wall_l:
                    table[i + 1][pos[i]] = 'W'
                elif i > wall_l:
                    table[i - 1][pos[i]] = 'W'

            if i - wall_l == pos[i] - wall_c:
                if i < wall_l and pos[i] < wall_c:
                    table[i + 1][pos[i] + 1] = 'W'
                elif i > wall_l and pos[i] > wall_c:
                    table[i - 1][pos[i] - 1] = 'W'
            if i - wall_l == wall_c - pos[i]:
                if i < wall_l and pos[i] > wall_c:
                    table[i + 1][pos[i] - 1] = 'W'
                elif i > wall_l and pos[i] < wall_c:
                    table[i - 1][pos[i] + 1] = 'W'

    table[wall_l][wall_c] = 'A'
    printTable()
