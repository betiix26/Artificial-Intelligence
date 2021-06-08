# -*- coding: utf-8 -*-

from functions import searchDFS
from functions import hash
import timeit


def main():
    start = timeit.default_timer()

    searchDFS(0)

    stop = timeit.default_timer()

    try:
       f = open('output.txt', 'a')
    except:
        print("ERROR")

    else:
        f.write('Time: ' + str(stop - start) + '\n')

if __name__ == "__main__":
    main()



