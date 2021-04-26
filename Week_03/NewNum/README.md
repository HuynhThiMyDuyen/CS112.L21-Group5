[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jMUvzcLbk3shmvXTl4nfmaZYp49eY1GA#scrollTo=bpAj5pkZBw24)

# **NEW NUMBER**

## **I. Abstraction (Trừu tượng hóa):**
- Tìm số `m lớn nhất chia hết cho 3` và `khác n` tại đúng `1 chữ số`.

## **II. Pattern Recognition (Nhận dạng mẫu):**
- **Bài toán/ Kỹ thuật:** Vét cạn.
- **Đặc điểm nhận dạng:**  
    - Duyệt qua từng chữ số đến khi tìm được chữ số lớn hơn thỏa đề bài.
    - Nếu không tìm chữ số nhỏ hơn chữ số cuối cùng và thỏa đề bài.   
    
## **III. ALgorithm Designed (Thiết kế thuật toán):**
**Mã giả:**
- Tách số n thành mảng các chữ số: `array = list(str(n))`.
- **Trường hợp 1:** Tìm số `m lớn hơn n` thỏa đề bài.  
Duyệt i từ vị trí đầu đến cuối mảng array:  
    - Gán `new` là số lớn hơn và gần giá trị `int(array[i])` nhất sao cho nếu thay `array[i] = new` ta có tổng mảng chia hết cho 3: `new = int(array[i]) + (3 - (n % 3))`.  
    - Nếu `new <= 9`:  
        - Tăng `new` thêm 3 đơn vị đến khi `new là lớn nhất có thể và bé hơn 10`.  
            - `while new <= 6:
                new += 3`  
        - Gán `array[i] = str(new)`.  
        - Gộp mảng thành `số m` và xuất ra màn hình.  
- **Trường hợp 2:** Tìm số `m bé hơn n` thoải đề bài.  
    - Nếu `n chia hết cho 3` thì gán `new = int(array[len(array) - 1]) - 3`.  
    - Nếu `n không chia hết cho 3` thì gán `new = int(array[len(array) - 1]) - (n % 3)`.  
    - Gán `array[len(array) - 1] = str(new)`.  
    - Gộp mảng thành `số m` và xuất ra màn hình.  

## **IV. Complexity (Độ phức tạp):**
- Gọi số nhập vào có `n chữ số`.
- Độ phức tạp của thuật toán: `O(n).`

## **V. Code:**
```python
def convertNewInteger(n):
    array = list(str(n))

    for i in range(len(array)):
        new = int(array[i]) + (3 - (n % 3))
        if new <= 9:
            while new <= 6:
                new += 3
                
            array[i] = str(new)
            print("".join(array))
            return

    if n % 3 == 0:
        new = int(array[len(array) - 1]) - 3
    else:
        new = int(array[len(array) - 1]) - (n % 3)
        
    array[len(array) - 1] = str(new)
    print("".join(array))

n = int(input())
convertNewInteger(n)
```


    123
    723

    
