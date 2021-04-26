def convertNewInteger(n):
    # convert a integer to array
    array = list(str(n))

    # find a new integer larger
    for i in range(len(array)):
        new = int(array[i]) + (3 - (n % 3))
        if new <= 9:
            while new <= 6:
                new += 3
                
            array[i] = str(new)
            print("".join(array))
            return

    # find a new integer smaller
    if n % 3 == 0:
        new = int(array[len(array) - 1]) - 3
    else:
        new = int(array[len(array) - 1]) - (n % 3)
        
    array[len(array) - 1] = str(new)
    print("".join(array))

# input
n = int(input())
convertNewInteger(n)