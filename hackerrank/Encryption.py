#!/bin/python3

import math
import os
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # remove spaces
    s = s.replace(" ", "")
    L = len(s)
    if L == 0:
        return ""
    root = math.sqrt(L)
    rows = math.floor(root)
    cols = math.ceil(root)
    if rows * cols < L:
        rows += 1
    # build encoded columns
    parts = []
    for c in range(cols):
        col_chars = []
        for r in range(rows):
            idx = r * cols + c
            if idx < L:
                col_chars.append(s[idx])
        parts.append(''.join(col_chars))
    return ' '.join(parts)

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')

    s = input().strip()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
