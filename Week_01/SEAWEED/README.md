# SEAWEED - TẢO BIỂN

## I. Abstraction (Trừu tượng hóa):
- Tìm số lượng cá thể sau k ngày với số lượng cá thể ban đầu là n.

## II. Pattern Recognition (Nhận dạng mẫu):
- **Bài toán/ Kỹ thuật:** Duyệt mảng
- **Đặc điểm nhận dạng:**  
Trường hợp **n = 1**, ta có:  
Bảng sinh sản của tảo biển như sau:  
|NGÀY / MỨC|  1  |  2  |  3  |  4  |  5  |  6  |  7  | SỐ CÁ THỂ |
|:--------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---------:|
|     0    |  1  |  -  |  -  |  -  |  -  |  -  |  -  |     1     |
|     1    |  1  |  1  |  -  |  -  |  -  |  -  |  -  |     2     |
|     2    |  3  |  1  |  1  |  -  |  -  |  -  |  -  |     5     |
|     3    |  8  |  3  |  1  |  1  |  -  |  -  |  -  |     13    |
|     4    |  13 |  8  |  3  |  1  |  1  |  -  |  -  |     34    |
|     5    |  34 |  13 |  8  |  3  |  1  |  1  |  -  |     89    |
|     6    |  89 |  34 |  13 |  8  |  3  |  1  |  1  |     233   |

  Bảng sinh sản của tảo biển theo mảng như sau:  

|MẢNG / k|  0  |  1  |  2  |  3  |  4  |  5  |  6  |
|:--------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  arr(k - 2)    |  -  |  -  |  1  |  2  |  5  |  13  |  34  |
|  arr(k - 1)    |  -  |  1  |  2  |  5  |  13  |  34  |  89  |
|3 * arr(k - 1) - arr(k - 2)|  1  |  2  |  5  |  13  |  34  |  89  | 233  |

## III. ALgorithm Designed (Thiết kế thuật toán):
**Mã giả:**
- Initialize:  
    `arr = [1, 2]`
- Loop from 1 to k:  
    `arr.insert(2, 3 * arr[1] - arr[0])`
    `arr.pop(0)`
- Print:  
    `(n * arr[1]) % (10**9 + 7)`

## IV. Complexity (Độ phức tạp):
- Vòng for chạy từ giá trị 1 đến k
- Độ phức tạp của thuật toán: `O(n)`