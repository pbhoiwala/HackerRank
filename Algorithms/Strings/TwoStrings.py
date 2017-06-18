# https://www.hackerrank.com/challenges/two-strings
n = int(input())
for i in range(n):
    a,b,found = input(), input(), False
    a,b = (a,b) if len(a)<len(b) else (b,a)
    for i in a:
        if i in b:
            found = True
            break
    print("YES" if found else "NO")
