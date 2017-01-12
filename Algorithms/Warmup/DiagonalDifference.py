#!/bin/python3
# https://www.hackerrank.com/challenges/diagonal-difference
import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

j = 0
k = n-1
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][j]
    sum2 += a[i][k]
    j+=1
    k-=1
print(abs(sum1-sum2))
