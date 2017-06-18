# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
import sys

def isDecent(num):
    fives, threes = [], []
    for n in num:
        fives.append(n) if n == '5' else threes.append(n)
    return (len(fives)%3==0) and (len(threes)%5==0)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = ['5']*n
    i, decent = len(arr)-1, isDecent(arr)
    while not decent and i > -1:
        arr[i],i = '3',i-1
        decent = isDecent(arr)
    print(''.join(arr) if decent else '-1')
