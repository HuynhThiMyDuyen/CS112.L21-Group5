# VR06_BOT
## I. Abstraction
- Tìm giá trị p và q sao cho mảng con arr[ p:q ] lớn nhất

## II. Pattern recognition
- Kadane's algorithm

## III. Algorithm designed
+ Initialize:  
    * max_so_far = 0  
    * max_ending_here = 0  
    * start = 0  
    * end = 0  
+ Loop for each element of the array
    * max_ending_here = mar_ending_here + arr[ i ]
    * if max_ending_here > max_so_far
        * max_so_far = max_ending_here
        * start = s
		* end = i
    * if max_ending_here < 0:
        * max_ending_here = 0	
		* s = i+1
+ return max_so_far

## IV. Complexity
+ O(n)

## V. Code



```python
n = int(input())
arr = list(map(int,input().split()))


def maxSubArraySum(a):
	max_so_far = -10**9 - 1
	max_ending_here = 0
	start = 0
	end = 0
	s = 0

	for i in range(n):

		max_ending_here += a[i]

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

		if max_ending_here < 0:
			max_ending_here = 0	
			s = i+1

	print (start+1,end+1,max_so_far)
maxSubArraySum(arr)
```

    16
    2 -4 5 -8 4 -1 -1 1 1 1 -2 2 4 -6 9 -4
    5 15 12
    
[![Open In Colab](https://drive.google.com/file/d/1J0Hrbc2nwcUozLSFr8_irpr3pSSNREbe/view?usp=sharing)]
