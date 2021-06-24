from fractions import Fraction

a, b, c, d = map(int, input().split())
if b == 0 or c == 0 or d == 0:
    print("Error")
else:
    print(Fraction(a * d, b * c))