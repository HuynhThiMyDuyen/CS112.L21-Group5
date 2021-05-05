from itertools import permutations

def MinSum(side, matrix):
          
    s = ''

    for i in range(0, side):
        s = s + str(i) 

    permlist = permutations(s)
      
    cases = []
      
    for perm in list(permlist):
        cases.append(''.join(perm))
      
    sum = []
      
    for c in cases:
        p = []
        tot = 0
        for i in range(0, side):
            p.append(matrix[int(s[i])][int(c[i])])
        p.sort()
        for i in range(side-1, -1, -1):
            tot = tot + p[i]
        sum.append(tot)
      
    print(min(sum)) 
  
n = int(input())
matrix = []
for i in range(n):
    l = list(map(int, input().split()))
    matrix.append(l)

MinSum(n, matrix)