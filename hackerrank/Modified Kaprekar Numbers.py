#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    res = []
    for n in range(p, q + 1):
        if n == 1:
            res.append(n)
            continue

        d = len(str(n))
        sq = n * n
        s = str(sq)

        r_str = s[-d:]
        l_str = s[:-d] if len(s) > d else "0"

        l = int(l_str) if l_str != "" else 0
        r = int(r_str)

        if l + r == n:
            res.append(n)

    if res:
        print(" ".join(str(x) for x in res))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
