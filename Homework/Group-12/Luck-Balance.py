N, K = map(int, input().strip().split())

luck = 0
important = []

for i in range(N):
    L, T = list(map(int, input().split()))
    if T == 0:
        luck += L
    else:
        important.append(L)
        
for i in sorted(important, reverse=True):
    if K > 0:
        luck += i
        K -= 1
    else:
        luck -= i

print(luck)