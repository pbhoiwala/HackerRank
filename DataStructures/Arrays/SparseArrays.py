# https://www.hackerrank.com/challenges/sparse-arrays
N = int(input())
strings = [input() for _ in range(N)]
Q = int(input())
queries = [input() for _ in range(Q)]

for q in queries:
    ctr=0
    for s in strings:
        if s in q: ctr+=1
    print(ctr)
