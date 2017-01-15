# https://www.hackerrank.com/challenges/designer-pdf-viewer
#!/bin/python3
import sys

h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()
alpha = list("abcdefghijklmnopqrstuvwxyz")
height = 0
for char in word:
    index = alpha.index(char)
    height = h[index] if h[index]>height else height
print(height*len(word))
