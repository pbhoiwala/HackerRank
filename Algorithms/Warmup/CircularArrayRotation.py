#!/bin/python3
# https://www.hackerrank.com/challenges/circular-array-rotation
import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for i in range(q):
    m = int(input().strip())
    off = m-k if (k <= len(a)) else m-(k%(len(a))
    print(a[off])
