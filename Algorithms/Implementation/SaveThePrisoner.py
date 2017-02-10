import sys
# https://www.hackerrank.com/challenges/save-the-prisoner
t = int(input())
for _ in range(t):
    n, m, s = map(int, input().split(" "))
    #print((s + m-1) % n) -- this won't work when modulo is 0
    print((s-1 + m-1) % n+1)
        
