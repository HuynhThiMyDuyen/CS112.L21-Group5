def maxSubArraySum(a,size):
    max_so_far = -999999999
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far


def maxSequence(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i

    if sum == 0:
        return max(arr)
    else:
        return sum


n = int(input())
l = list(map(int, input().split()))
print(maxSubArraySum(l, n))
print(maxSequence(l))