n, m = map(int,input().split())
d = {i:[] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

val = [1 for i in range(n + 1)]
par = [-1 for i in range(n + 1)]
par[1] = 1
stack = [1]
while stack:
    u = stack[-1]
    f = 0
    for i in d[u]:
        if par[i] == -1:
            par[i] = u
            stack.append(i)
            f = 1
    if f == 0:
        stack.pop()
        val[par[u]] += val[u]
ans = 0
for i  in range(2, n + 1):
    if val[i] % 2 == 0:
        ans += 1
print(ans)