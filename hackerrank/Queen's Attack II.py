#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    up = n - r_q
    down = r_q - 1
    right = n - c_q
    left = c_q - 1
    up_right = min(up, right)
    up_left = min(up, left)
    down_right = min(down, right)
    down_left = min(down, left)

    obs = {(r, c) for r, c in obstacles}

    def walk(dr, dc, limit):
        steps = 0
        r, c = r_q, c_q
        for _ in range(limit):
            r += dr
            c += dc
            if (r, c) in obs:
                break
            steps += 1
        return steps

    total = 0
    total += walk(1, 0, up)
    total += walk(-1, 0, down)
    total += walk(0, 1, right)
    total += walk(0, -1, left)
    total += walk(1, 1, up_right)
    total += walk(1, -1, up_left)
    total += walk(-1, 1, down_right)
    total += walk(-1, -1, down_left)

    return total

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
