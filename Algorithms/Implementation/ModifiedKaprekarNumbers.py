# https://www.hackerrank.com/challenges/kaprekar-numbers/
p = int(input())
q = int(input())
valid = False
for i in range(p,q+1,1):
    sqr = str(i*i)
    mid = len(sqr)//2
    a,b = sqr[:mid], sqr[mid:]
    a = 0 if a == '' else int(a)
    b = int(b)
    if a+b == i:
        valid = True
        print(i,end=" ")
if not valid: print("INVALID RANGE")
