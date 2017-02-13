#!/bin/python3
# https://www.hackerrank.com/challenges/append-and-delete/
import sys

s = input().strip()
t = input().strip()
k = int(input().strip())
if (len(s)-len(t)) % 2 != 0 and k %2 == 0: # special case
    print('No') 
    sys.exit()
a,b = (s[:], t[:]) if len(s)>=len(t) else (t[:],s[:])
i=0
while i < len(b):
    if a[i] != b[i]: break
    i+=1
oper = len(a)-i + len(b[i:])
print('Yes' if oper<=k else 'No')