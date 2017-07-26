# https://www.hackerrank.com/challenges/maximum-element/
n = int(input())
stack = []

def getFirst():
    if stack: return stack[-1]
    return -1

for _ in range(n):
    q = list(map(int,input().split()))
    if q[0] == 1:
        stack.append(max(q[1],getFirst()))   # only store the max item in stack
    elif q[0] == 2:
        if stack:stack.pop()
    elif q[0] == 3:
        print(getFirst())
