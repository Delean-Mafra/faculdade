#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # calcula e imprime o fatorial usando inteiros arbitrariamente grandes do Python
    print(math.factorial(n))

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)
