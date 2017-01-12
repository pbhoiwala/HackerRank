#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = neg = zeroes = 0
for i in arr:
    if i > 0:
        pos +=1
    elif i < 0:
        neg +=1
    else:
        zeroes+=1
print(float(pos/n))
print(float(neg/n))
print(float(zeroes/n))