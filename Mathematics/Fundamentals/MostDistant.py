# https://www.hackerrank.com/challenges/most-distant

import math
n = int(input())
xNeg,xPos,yNeg,yPos = 0,0,0,0

for _ in range(n):
    point = list(map(int,input().split()))
    xNeg, xPos = min(xNeg,point[0]), max(xPos,point[0])
    yNeg, yPos = min(yNeg,point[1]), max(yPos,point[1])

farPoints = [[xNeg,0],[xPos,0],[0,yNeg],[0,yPos]]
    
def getDistance(a,b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    return abs(math.sqrt(x**2 + y**2))

m = float(0)
for a in farPoints:
    for b in farPoints:
        m = max(m,getDistance(a,b))
print("%.6f" % m)
