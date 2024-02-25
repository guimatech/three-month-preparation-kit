#!/bin/python3

import os

def breakingRecords(scores):
    countMin, countMax = 0, 0

    minScore = scores[0]
    maxScore = scores[0]

    for score in scores:
        if score < minScore:
            minScore = score
            countMin += 1

        if score > maxScore:
            maxScore = score
            countMax += 1

    return [countMax, countMin]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
