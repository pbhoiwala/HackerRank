# https://www.hackerrank.com/challenges/sherlock-and-array/

T = int(input())
for _ in range(T):
    n = int(input())
    A = [int(i) for i in input().strip().split(' ')]
    if(len(A) == 1 or A[0] == A[-1]): # this is for case when A has only 1 number (test case #6)
        print("YES")
        continue
    found = False
    before = sum(A[0:1])
    after = sum(A[2:])
    for i in range(2, n,1):
        before += A[i-1] 
        after -= A[i]
        found = before == after
        if(found): break
    print("YES" if found else "NO")
