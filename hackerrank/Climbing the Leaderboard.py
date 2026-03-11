#!/bin/python3

import os
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Remove duplicates while preserving descending order
    unique_scores = []
    prev = None
    for s in ranked:
        if s != prev:
            unique_scores.append(s)
            prev = s

    result = []
    i = len(unique_scores) - 1  # pointer starting at the lowest unique score

    for score in player:
        # Move pointer left while player's score is >= current unique score
        while i >= 0 and score >= unique_scores[i]:
            i -= 1
        # rank is i+2 (if i == -1 then rank = 1)
        result.append(i + 2)

    return result

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')

    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
