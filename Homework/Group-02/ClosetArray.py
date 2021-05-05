def findClosetArray(arr, target):
    current_result = sum(arr) - target
    result = current_result
    while arr:
        arr.sort(key = lambda x : abs(x - current_result))
        arr.pop(0)
        current_result = sum(arr) - target
        if abs(result) > abs(current_result):
            result = current_result
    print(abs(result)) 


string = input()
target = int(input())

arr = []
i = 0
tem = ""
while i < len(string):
    if string[i] == '-':
        tem += string[i]
        i += 1
    elif string[i].isdigit():
        tem += string[i]
        i += 1
    else:
        if tem != "":
            arr.append(int(tem))
        i += 1
        tem = ""
        
print(arr)
findClosetArray(arr, target)