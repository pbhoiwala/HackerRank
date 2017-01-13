# https://www.hackerrank.com/challenges/extra-long-factorials
#!/bin/python3

import sys

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
    
n = int(input().strip())
print(fact(n))
