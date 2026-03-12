#!/bin/python3

import math
import os
import sys

def formingMagicSquare(s):
    # All 8 possible 3x3 magic squares using numbers 1..9
    magic_squares = [
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,7,6],[9,5,1],[4,3,8]]
    ]

    min_cost = math.inf
    for magic in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])
        if cost < min_cost:
            min_cost = cost

    return int(min_cost)

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')

    s = []
    for _ in range(3):
        s.append(list(map(int, sys.stdin.readline().rstrip().split())))

    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()
