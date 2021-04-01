n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse = True)

while n > 0:
    if arr[n - 1] >= n:
        print(n)
        break
    else:
        n -= 1

if n == 0:
    print(n)