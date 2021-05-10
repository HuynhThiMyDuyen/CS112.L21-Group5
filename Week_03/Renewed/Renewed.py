a, k, b, m, n = map(int, input().split())

c = a + b
# calculate amount of trees in k * m day
day = k * m
amount_of_trees = day * c - (day // k) * a - (day // m) * b

# find the result
if n % amount_of_trees == 0:
    print((n // amount_of_trees) * day - 1)
    return

day = (n * day) // amount_of_trees - 1
while True:
    amount_of_trees = day * c - (day // k) * a - (day // m) * b
    if amount_of_trees >= n:
        print(day)
        break
    else:
        day += 1