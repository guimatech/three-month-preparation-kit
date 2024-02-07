#!/bin/python3

def miniMaxSum(arr):
    mainSum = sum(arr, 0)
    minValue = min(arr)
    maxValue = max(arr)
    print(f'{mainSum - maxValue} {mainSum - minValue}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
