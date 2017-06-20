# https://www.hackerrank.com/challenges/circular-array-rotation
import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

def rotateArray(array, k):
    newArr = []
    for i in range(len(array)):
        if k > len(array):
            newArr.append(array[i-k + len(array)])
        else:
            newArr.append(array[i-k])
    return newArr

 for i in range(q):
    m = int(input().strip())
    if(k<=len(a)):
        off = m-k
    else:
        off = m-(k%(len(a)))
    print(a[off])