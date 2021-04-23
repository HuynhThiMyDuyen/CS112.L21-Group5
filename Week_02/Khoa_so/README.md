[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18adNq7cg6xO8WoBXetw-a2HT19gLpUPz#scrollTo=r719KpPrA6Hd)
# KHOA SO
## I. Abstraction
  * Find the largest string of numbers divisible by 3

## II. Pattern recognition
  * Skill: Browsing array
  * Pattern recognition: numbers divisible by 3
   
## III. Algorithm designed
  * Covert string to list:
      + for i in string: append(int(i)) to arr
  * Sort arr: arr.sort()
  * Find modulo
      + r = a%3 for a in arr
  * Initialize def remove x in array r and remove value with index = r.index(x) in array arr
  * Case 1: sum modulo % 3 == 0:
      + arr.sort(reverse = True)
      + print(*arr,sep=())
  * Case 2: sum modulo % 3 != 0:
      + try: remove number smallest with (s = sum modulo % 3 = ( 1 or 2 )) 
      + else => except: remove 2 number smallest with (s = 3 - sum modulo % 3)
      + then arr.sort(reverse = True)
      + print(*arr,sep =())
 
## IV. Complexity
   * O(n)
   * 
## V. Code

```python
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
        
# Driver Code

string = list(input().strip())

arr = []
for i in string:
    arr.append(int(i))
arr.sort()
largestMultipleOfThree(arr)
```


    105
    510
    
