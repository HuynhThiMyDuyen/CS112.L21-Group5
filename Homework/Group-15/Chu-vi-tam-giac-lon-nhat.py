#!/bin/python3

import math
import os
import random
import re
import sys

def max_chuvi_tamgiac(sticks):
    n = len(sticks)
    max_perimeter = -1
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                a, b, c = sticks[i], sticks[j], sticks[k]
                if (a + b > c and a + c > b and b + c > a):
                    max_perimeter = max(max_perimeter, a + b + c)
    return max_perimeter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = max_chuvi_tamgiac(sticks)

    fptr.write(str(result) + '\n')

    fptr.close()
