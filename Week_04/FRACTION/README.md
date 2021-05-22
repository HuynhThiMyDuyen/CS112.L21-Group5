<a href="https://colab.research.google.com/" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# VU20_FRACTION

## I. ABSTRACTION (TRỪU TƯỢNG HÓA)  
- Input: Cho phân số a/b và c/d tối giản (0 < a < b < 10^5, 0 < c < d < 10^5)
- Process: Mỗi lần tăng a, b lên 1 đơn vị và tối giản a/b
- Output: Tìm số process để a/b = c/d (Nếu không có process nào thì xuất 0)

## II. PATTERN RECOGNIZATION (NHẬN DIỆN KHUÔN MẪU)
- Kỹ thuật: Duyệt

## III. Algorithm designed
- Khởi tạo hàm tìm UCLN của 2 số a và b:  
    + Nếu b == 0 => return a  
    + Đệ quy return ucln(b, a%b)
- Hàm xử lý:
    + Khởi tạo biến đếm count = 0
    + f1 = a/b
    + f2 = c/d
    + Trong khi f1 < f2: 
        + a = a + 1
        + b = b + 1
        + Nếu a / b = c / d => Xuất count và thoát
        + Nếu sai thì count += 1 và lặp lại
    + Nếu f1 < f2: Xuất 0



## IV. Complexity  
- O(2 * max(b, d))

## V. Code


```python
def ucln(a, b):
    if (b == 0):
        return a
    return ucln(b, a % b)

def fraction(a,b,c,d):
    count = 1
    f1 = a / b
    f2 = c / d
    while f1 < f2:
        a += 1
        b += 1
        k = ucln(a, b)
        a /=k
        b /= k
        f1 = a / b
        if f1 == f2:
            return count
        count+=1
    if f1 != f2:
        return 0


# Drive code
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(fraction(a,b,c,d))
```

    1
    6
    2
    3
    5
    
