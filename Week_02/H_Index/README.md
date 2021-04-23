[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rQsGB7d3bzF3oa_Rmeu0Wfv2UoOBURPS#scrollTo=gNWPio0_05wo)
# **H-INDEX**
## **I. Abstraction (Trừu tượng hóa):**
- Tìm số `k lớn nhất` sao cho mảng `n` có `k` số có giá trị `lớn hơn hoặc bằng k`.

## **II. Pattern Recognition (Nhận dạng mẫu):**
- **Bài toán/ Kỹ thuật:** Duyệt mảng
- **Đặc điểm nhận dạng:**  
Ví dụ cho mảng arr = [2, 4, 5, 6, 7, 3, 9].

	- Với `k = 7` có `2` phần tử `>= 7` => `không thỏa.`  
	- Với `k = 6` có `3` phần tử `>= 6` => `không thỏa.`  
	- Với `k = 5` có `4` phần tử `>= 5` => `không thỏa.`  
	- Với `k = 4` có `5` phần tử `>= 4` => `thỏa.`  
	- Với `k = 3` có `6` phần tử `>= 3` => `thỏa.`  
	- Với `k = 2` có `7` phần tử `>= 2` => `thỏa.`  
	- Với `k = 1` có `7` phần tử `>= 1` => `thỏa.`  

	Vậy `k = 4` thỏa yêu cầu đề.

## **III. ALgorithm Designed (Thiết kế thuật toán):**
**Mã giả:**
- Sắp xếp mảng giảm dần: `arr.sort(reverse = True)`.
- Loop `n > 0:`  
	Nếu `arr[n - 1] >= n:` thì `print(n)` và dừng chương trình.  
	Nếu `arr[n - 1] < n:` thì `n -= 1`.
- Nếu `n == 0:` thì `print(0)`.
## **IV. Complexity (Độ phức tạp):**
- Độ phức tạp của thuật toán: `O(n).`
## **V. Code**
```python
n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse = True)

while n > 0:
    if arr[n - 1] >= n:
        print(n)
        break
    else:
        n -= 1

if n == 0:
    print(n)
```


    5
    8 5 3 4 10
    4
    
    
