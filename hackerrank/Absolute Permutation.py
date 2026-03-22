#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n + 1))
    
    if n % (2 * k) != 0:
        return [-1]
    
    result = []
    add = True  # alterna entre adicionar k e subtrair k
    for i in range(1, n + 1):
        if add:
            result.append(i + k)
        else:
            result.append(i - k)
        
        # alterna a cada bloco de tamanho k
        if i % k == 0:
            add = not add
    
    return result


# Testando com os exemplos:
print(absolutePermutation(2, 1))  # [2, 1]
print(absolutePermutation(3, 0))  # [1, 2, 3]
print(absolutePermutation(3, 2))  # [-1]
print(absolutePermutation(4, 2))  # [3, 4, 1, 2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
