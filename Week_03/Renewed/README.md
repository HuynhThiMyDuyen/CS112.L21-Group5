[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jGhkde79Z9XAzzuCHKYzmpG5c-GosHeW#scrollTo=fM1Mm7vStaCM)

# **RENEWED**

## **I. Abstraction (Trừu tượng hóa):**
- Tìm `số ngày` 2 đội đốn hết `n cây xanh`, biết đội I hạ được `a cây` mỗi ngày, cứ mỗi `ngày thứ k` thì nghỉ và đội II hạ được `b cây` mỗi ngày, cứ mỗi `ngày thứ m` thì phải nghỉ.
    - Tổng số cây 2 đội đốn 1 ngày: `c = a + b`.
    - Số cây 2 đội đốn `day = k * m` ngày: `amount_of_trees = day * c - (day // k) * a - (day // m) * b`.
    - Số ngày tối thiểu để đốn hết `n cây xanh`: `day = (n * day) // amount_of_trees - 1`.

## **II. Pattern Recognition (Nhận dạng mẫu):**
- **Bài toán/ Kỹ thuật:** Chia để trị.
- **Đặc điểm nhận dạng:**  
    - Tìm ra khoảng ngày mà 2 đội đốn hết cây.
    - Duyệt từ đầu đến cuối khoảng sao cho số cây 2 đội đốn `lớn hơn hoặc bằng n`.    
    
## **III. ALgorithm Designed (Thiết kế thuật toán):**
**Mã giả:**
- Số cây đốn hạ 1 ngày: `c = a + b`.
- Số cây đốn hạ `day = k * m` ngày: `amount_of_trees = day * c - (day // k) * a - (day // m) * b`.
- Số ngày tối thiểu để đốn hạ: `day = (n * day) // amount_of_trees - 1`.
- Nếu `n % amount_of_trees == 0` thì xuất `day` ra màn hình và dừng chương trình
- Nếu `n % amount_of_trees != 0` thì thực hiện `loop`:
    - Tính lượng cây đốn hạ trong `day` ngày: `amount_of_trees = day * c - (day // k) * a - (day // m) * b`.
    - Nếu `amount_of_trees >= n` thì xuất `day` ra màn hình và dừng chương trình.
    - Nếu `amount_of_trees < n` thì `day = day + 1`.

## **IV. Complexity (Độ phức tạp):**
- Độ phức tạp của thuật toán: `O(logn).`

## **V. Code:**
```python
a, k, b, m, n = map(int, input().split())

c = a + b
# calculate amount of trees in k * m day
day = k * m
amount_of_trees = day * c - (day // k) * a - (day // m) * b

# find the result
if n % amount_of_trees == 0:
    print((n // amount_of_trees) * day - 1)
    return

day = (n * day) // amount_of_trees - 1
while True:
    amount_of_trees = day * c - (day // k) * a - (day // m) * b
    if amount_of_trees >= n:
        print(day)
        break
    else:
        day += 1
```


    2 4 3 3 25
    7
