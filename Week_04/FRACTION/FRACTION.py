def ucln(a, b):
    if (b == 0):
        return a
    return ucln(b, a % b)

def fraction(a,b,c,d):
    count = 1
    f1 = a / b
    f2 = c / d
    while f1 < f2:
        a += 1
        b += 1
        k = ucln(a, b)
        a /=k
        b /= k
        f1 = a / b
        if f1 == f2:
            return count
        count+=1
    if f1 != f2:
        return 0


# Drive code
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(fraction(a,b,c,d))