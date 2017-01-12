#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

aliceList = [a0, a1, a2]
bobList = [b0, b1, b2]
alice = bob = 0
for i in range(0,3,1):
    if(aliceList[i] > bobList[i]):
        alice += 1
    elif(aliceList[i] < bobList[i]):
        bob += 1
  

print(str(alice) + " " + str(bob))