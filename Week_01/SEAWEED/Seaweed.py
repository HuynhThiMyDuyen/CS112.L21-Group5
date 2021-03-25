n, k = map(int, input().split())

arr = [1,2]
for i in range(1, k):
    arr.insert(2, 3 * arr[1] - arr[0])
    arr.pop(0)

print((n * arr[1]) % (10**9 + 7))
