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