#!/bin/python3

import math
import os
import random
import re
import sys

def min_swaps(arr):
    count = 0
    min_ele = min(arr)
    for i in range(len(arr)):
        while arr[i] != i + min_ele:
            swap_index = arr[i] - min_ele
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = min_swaps(arr)

    fptr.write(str(result) + '\n')

    fptr.close()