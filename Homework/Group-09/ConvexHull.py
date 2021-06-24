from sys import stdin, stdout

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
def Left_index(points):
    minn = 0
    for i in range(1,len(points)):
        if points[i].y < points[minn].y:
            minn = i
        elif points[i].y == points[minn].y:
            if points[i].x < points[minn].x:
                minn = i
    return minn
  
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)
  
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def PolygonArea(corners):
    n = len(corners) 
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

  
def convexHull(points, n):
    if n < 3:
        return
  
    l = Left_index(points)
  
    hull = []
      
    p = l
    q = 0
    while(True):
        hull.append(p)
        q = (p + 1) % n
        for i in range(n):
            if(orientation(points[p], points[i], points[q]) == 2):
                q = i
        p = q
  
        if(p == l):
            break
  
    polygon = []
    polygon.append((points[hull[0]].x, points[hull[0]].y))
    start = 0
    i = 1
    end = 2
    while end < len(hull):
        if (orientation(points[hull[start]], points[hull[i]], points[hull[end]]) != 0):
            polygon.append((points[hull[i]].x, points[hull[i]].y))
            start = i
            i += 1
            end += 1
        else:
            i += 1
            end += 1
    if (orientation(points[hull[start]], points[hull[i]], points[hull[0]]) != 0):
            polygon.append((points[hull[end]].x, points[hull[end]].y))

    print(len(polygon))
    print(PolygonArea(polygon))
    for x in polygon:
        stdout.write(str(x[0]) + ' ' + str(x[1]) + '\n')
  
# Driver Code
n = int(input())
points = []
for i in range(n):
    p = list(map(int, input().split()))
    points.append(Point(p[0], p[1]))
  
convexHull(points, len(points))