#!/bin/python3

import os
import sys

def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])
    g = [list(row) for row in grid]

    pluses = []

    for i in range(n):
        for j in range(m):
            if g[i][j] != 'G':
                continue

            cells = {(i, j)}
            pluses.append((1, cells))

            arm = 1
            while True:
                up = i - arm
                down = i + arm
                left = j - arm
                right = j + arm

                if up < 0 or down >= n or left < 0 or right >= m:
                    break

                if (g[up][j] != 'G' or g[down][j] != 'G' or
                        g[i][left] != 'G' or g[i][right] != 'G'):
                    break

                new_cells = set(cells)
                new_cells.update([(up, j), (down, j), (i, left), (i, right)])
                cells = new_cells
                area = len(cells)
                pluses.append((area, cells))

                arm += 1

    max_prod = 0
    L = len(pluses)
    for i in range(L):
        area1, cells1 = pluses[i]
        for j in range(i + 1, L):
            area2, cells2 = pluses[j]
            if cells1.isdisjoint(cells2):
                prod = area1 * area2
                if prod > max_prod:
                    max_prod = prod

    return max_prod


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    grid = []
    for _ in range(n):
        grid_item = input().strip()
        grid.append(grid_item)

    result = twoPluses(grid)

    print(result)
