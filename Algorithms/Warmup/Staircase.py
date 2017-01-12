#!/bin/python3

import sys


n = int(input().strip())

for i in range(1,n+1,1):
    for j in range(n,0,-1):
        if(j > i):
            print(" ",end='')
        else:
            print("#",end='')
    print('')