# https://www.hackerrank.com/challenges/missing-numbers
import sys
from collections import OrderedDict
n = int(input())
A = input().split()
m = int(input())
B = input().split()

A.sort(reverse=True)
B.sort(reverse=True)
p = OrderedDict()
j = 0
for i in range(m):
    if B[i] != A[j]:
        p[B[i]] = '';
    else:
        j+=1

for s in reversed(p):
    print(s, end=" ")
