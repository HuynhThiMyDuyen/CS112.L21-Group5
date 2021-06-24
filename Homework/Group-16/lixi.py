def can_partition(num):
    s = sum(num)

    for i in num:
        if i <= 0:
            return False
    if s % 2 != 0:
        return False

    s = int(s / 2)

    n = len(num)
    dp = [[False for x in range(s+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = True

    for j in range(1, s+1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]: 
                dp[i][j] = dp[i - 1][j - num[i]]


    return dp[n - 1][s]


n = int(input())
number = [int(x) for x in input().split()]
print(can_partition(number))

