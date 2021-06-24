#!/bin/python3

import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    # Write your code here
    for i in range(len(arr)):
        for j in range(len(brr)):
            if arr[i] == brr[j]:
                del brr[j]
                break
    brr = list(dict.fromkeys(brr))
    brr.sort()
    return brr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()