#!/bin/python3
# https://www.hackerrank.com/challenges/time-conversion
import sys


time = input().strip()

hour = time[0]+time[1]
newHour = hour
if ('PM' in time) and (1 <= int(hour) <= 11):
    newHour = str(int(hour)+12)
elif ('AM' in time) and (int(hour) is 12):
    newHour = '00'
print(newHour + time[2:8])
