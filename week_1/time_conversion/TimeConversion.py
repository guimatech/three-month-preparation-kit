#!/bin/python3

import os


def timeConversion(s):
    hour, minute, second = [int(x) for x in s[:-2].split(':')]
    isPM = s[-2:] == 'PM'

    if (isPM and hour != 12) or (not isPM and hour == 12):
        hour += 12
    if hour >= 24:
        hour -= 24

    return f'{hour:02d}:{minute:02d}:{second:02d}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
