# https://www.hackerrank.com/challenges/an-interesting-game-1/submissions/code/43717664
import sys

def findMaxIndex(array):
    m = 0
    index = 0
    for i in range(len(array)):
        m = array[i] if array[i] > m else m
        index = i
    return index

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    array = [int(i) for i in input().split(' ')]
    player = 1 # 0 is Bob, 1 is Andy, Start with Bob's turn
    maxCount,maxValue = 0,0
    for i in range(len(array)):
        if array[i] > maxValue:
            maxValue = array[i]
            maxCount += 1
            player = not player
    print("ANDY" if player else "BOB")
