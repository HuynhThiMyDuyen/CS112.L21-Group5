def segmentUnionLength(segments):
    n = len(segments)
    points = [None] * (n * 2)
     
    for i in range(n):
        points[i * 2] = (segments[i][0], False)
        points[i * 2 + 1] = (segments[i][1], True)
         
    points = sorted(points, key=lambda x: x[0])
     
    result = 0
     
    Counter = 0
     
    for i in range(0, n * 2):
        if (i > 0) & (points[i][0] > points[i - 1][0]) &  (Counter > 0):
            result += (points[i][0] - points[i - 1][0])
             
        if points[i][1]:
            Counter -= 1
        else:
            Counter += 1
    return result
 
 
# Driver code

segments = [(2, 5), (4, 8), (9, 12)]
print(segmentUnionLength(segments))