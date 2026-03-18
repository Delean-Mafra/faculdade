#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # convert to list for swapping
    s = list(w)
    n = len(s)

    # 1) find pivot i
    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    if i == -1:
        return "no answer"

    # 2) find j: smallest char greater than s[i] to the right
    j = n - 1
    while s[j] <= s[i]:
        j -= 1

    # 3) swap
    s[i], s[j] = s[j], s[i]

    # 4) reverse suffix i+1..end
    s[i + 1:] = reversed(s[i + 1:])

    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')

    fptr.close()
