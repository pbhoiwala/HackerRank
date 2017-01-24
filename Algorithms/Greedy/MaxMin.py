# https://www.hackerrank.com/challenges/angry-children
import sys

n = int(input())
k = int(input())
myList = [int(input()) for _ in range(n)]
myList.sort()

diff = max(myList)
p = 0
while p < (n-k+1):
    diff = min((myList[p+k-1] - myList[p]), diff)
    p+=1
print(diff)
