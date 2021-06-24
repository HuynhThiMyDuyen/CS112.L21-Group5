from math import *

a, b, c = map(int, input().split())

if a == 0:

    if b == 0:
        if c == 0:
            print("VSN")
        else:
            print("VN")
    
    else:
        result = -c / b
        if result == int(result):
            print(int(result))
        else:
            print(round(result, 2))
else:

    denta = b**2 - 4 * a * c

    if denta < 0:
        print("VN")

    elif denta == 0:
        result = (-b) / (2 * a)
        if result == int(result):
            print(int(result))
        else:
            print(round(result, 2))
            
    else:
        result_1 = (-b - sqrt(denta)) / (2 * a)
        result_2 = (-b + sqrt(denta)) / (2 * a)
        if result_1 == int(result_1):
            result_1 = int(result_1)
        else:
            result_1 = round(result_1, 2)
        if result_2 == int(result_2):
            result_2 = int(result_2)
        else:
            result_2 = round(result_2, 2)
        print(result_1, result_2)