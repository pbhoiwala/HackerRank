#!/bin/python3
# https://www.hackerrank.com/challenges/a-very-big-sum
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(sum(arr))
