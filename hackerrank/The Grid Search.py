#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    R = len(G)
    r = len(P)
    if r == 0:
        return "YES"
    c = len(P[0])

    # For each possible starting row in G
    for i in range(R - r + 1):
        start = 0
        # find all occurrences of P[0] in G[i]
        while True:
            idx = G[i].find(P[0], start)
            if idx == -1:
                break
            # check subsequent rows
            match = True
            for k in range(1, r):
                if G[i + k][idx:idx + c] != P[k]:
                    match = False
                    break
            if match:
                return "YES"
            start = idx + 1
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input().strip()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input().strip()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
