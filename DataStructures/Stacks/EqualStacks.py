# https://www.hackerrank.com/challenges/equal-stacks/
import sys

def getTop(stack):
    return stack[-1] if stack else 0

def fillStack(arr):
    s = []
    while(arr): s.append(arr.pop() + getTop(s))
    return s

n1,n2,n3 = input().split(' ')
h1 = list(map(int,input().split()))
h2 = list(map(int,input().split()))
h3 = list(map(int,input().split()))

s1 = fillStack(h1)
s2 = fillStack(h2)
s3 = fillStack(h3)

while s1 and s2 and s3:
    m1, m2, m3 = getTop(s1), getTop(s2), getTop(s3)
    if m1 == m2 == m3:
        print(m1)
        exit()
    m = max(m1, m2, m3)
    if m1 == m: s1.pop()
    if m2 == m: s2.pop()
    if m3 == m: s3.pop()
print(0)
