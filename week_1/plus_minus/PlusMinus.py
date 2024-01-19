#!/bin/python3

def plusMinus(arr, n):
    pos, neg, zero = 0, 0, 0

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    print(f'{pos/n:.6f} \n{neg/n:.6f} \n{zero/n:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
