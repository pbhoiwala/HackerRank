# https://www.hackerrank.com/challenges/sherlock-and-valid-string
s = input()
unique = list(set(s))
maxx = list(s).count(s[0]) # max number of occurences for a char allowed
broken=False               # condition broken or no
oneRemoved=False           # one char deletion allowed
for u in unique:
    if(list(s).count(u) != maxx):
        if oneRemoved:
            broken = True       
            break
        else: oneRemoved=True
print('YES' if not broken else 'NO')
