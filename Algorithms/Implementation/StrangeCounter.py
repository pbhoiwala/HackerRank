#!/bin/python3
# https://www.hackerrank.com/challenges/strange-code
import sys
t = int(input().strip())
initT, initV, endT = 1,3,3 # initialize vars from col 1
col=1
while not(initT <= t <= endT):  # loop until the column with proper range is not found
    col+=1
    initV *= 2
    initT = initV-2
    endT = initT + initV - 1
print(initV-(t-initT))
