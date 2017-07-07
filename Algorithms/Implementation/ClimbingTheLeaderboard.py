# https://www.hackerrank.com/challenges/climbing-the-leaderboard
import sys

n = int(input())
scores = sorted(set(map(int,input().split())),reverse=True)
m = int(input())
alice = list(map(int,input().split()))

j = 0
while(j < m):
    if not scores:
        j+=1
        print(1)
        continue
    score = scores.pop()
    if alice[j] <= score:
        scores.append(score)
        if alice[j] != score: scores.append(alice[j])
        j+=1
        print(len(scores))
