# https://www.hackerrank.com/challenges/maxsubarray

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # bestSoFar: largest sum of any contiguous subarray so far
    # prevSubmax: sum of previous subarray (not including current i)
    bestSoFar, prevSubMax = 0,0
    # maxPosSum: non-contigous sub array sum = sum of positive nums
    # maxNegNum: largest negative number in a, edge case
    maxPosSum, maxNegNum = 0, -10001  
    for i in a:
        if i > 0: maxPosSum += i
        if i < 0: maxNegNum = max(maxNegNum, i)
        bestSoFar = max(bestSoFar, prevSubMax + i, i)
        prevSubMax = max(prevSubMax + i, 0)
    
    # edge case: when sum = 0 or when all nums in a are neg
    if bestSoFar == 0: bestSoFar = maxNegNum
    if maxPosSum == 0: maxPosSum = maxNegNum
    print(bestSoFar, maxPosSum)  
