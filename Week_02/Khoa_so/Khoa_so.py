def remove_smallest(x,r,arr):
        idx = r.index(x)
        arr.pop(idx)
        r.pop(idx)

def largestMultipleOfThree(arr):
    r = [a % 3 for a in arr]
    s = sum(r) % 3

    if s != 0:
        try:
            remove_smallest(s, r, arr)
        except:
            remove_smallest(3-s, r, arr)
            remove_smallest(3-s, r, arr)

    if len(arr) == 0:
        print("")
    else:
        arr.sort(reverse = True)
        print(*arr,sep="")


from sys import stdin

string = list(stdin.readline().strip())
arr = []
for i in string:
    arr.append(int(i))
arr.sort()
largestMultipleOfThree(arr)
