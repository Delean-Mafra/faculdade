#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])

    board = [list(row) for row in grid]

    if n == 1:
        return grid

    if n % 2 == 0:
        return ['O' * c for _ in range(r)]

    def explode(b):
        to_clear = [[False]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if b[i][j] == 'O':
                    to_clear[i][j] = True
                    if i > 0:
                        to_clear[i-1][j] = True
                    if i < r-1:
                        to_clear[i+1][j] = True
                    if j > 0:
                        to_clear[i][j-1] = True
                    if j < c-1:
                        to_clear[i][j+1] = True
        res = [['O']*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if to_clear[i][j]:
                    res[i][j] = '.'
        return res

    first_explosion = explode(board)
    second_explosion = explode(first_explosion)

    if n % 4 == 3:
        return [''.join(row) for row in first_explosion]
    else:
        return [''.join(row) for row in second_explosion]

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
