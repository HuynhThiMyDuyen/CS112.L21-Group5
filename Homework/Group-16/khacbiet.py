def SolveSolution(List):
    n=len(List)
    k=0
    b=[]
    for i in range(n):
        for j in range(len(List[i])):
            b.append([List[i][j], i])
    b.sort()
    
    d=[0 for i in range(n)]
    j=0
    res=999
    for i in range(len(b)):
        if (d[b[i][1]]==0):
            k+=1
        d[b[i][1]]+=1
        while (k==n):
            res = min(res, b[i][0]-b[j][0])
            d[b[j][1]]-=1
            if (d[b[j][1]]==0):
                k-=1
            j+=1
    return res
n=int(input())
List=[]
for i in range(n):
    arr = [int(x) for x in input().split()]
    List.append(arr)
#List=[[28,46,89],[83],[30,64]]
a=SolveSolution(List)
print(a)