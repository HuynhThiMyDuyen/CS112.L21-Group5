def findHeightofSawBlade(arr, n, wood):
    arr.sort(reverse = True)
    # arr_2 contains disparity height between close trees from descended arr
    arr_2 = []
    for i in range(n - 1):
        arr_2.append(arr[i] - arr[i + 1])
    arr_2.append(arr[n - 1])

    # count amount of wood if cut from highest tree to lowest tree.
    current_wood = 0 
    for i in range(n):
        current_wood += arr_2[i] * (i + 1)
        if current_wood >= wood:
            height_sparewood = int((current_wood - wood) / (i + 1)) 
            if i == n - 1:
                print(height_sparewood)
                break
            else:
                print(arr[i + 1] + height_sparewood)
                break

# input
n, m = map(int, input().split())
arr = list(map(int, input().split()))

findHeightofSawBlade(arr, n, m)
