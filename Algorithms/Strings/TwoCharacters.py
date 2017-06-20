# https://www.hackerrank.com/challenges/two-characters/submissions/code/47261036
import sys

s_len = int(input().strip())
s = input().strip()

# special cases
if (len(s) <= 2):
    print(0 if len(s) < 2 else 2)
    exit()
    
# check to see if the string contains any 'same' consecutive characters
def consecCheck(s):
    return any(c1 == c2 for c1, c2 in zip(s, s[1:]))

# removes all the characters in string s except the two special ones to keep
def replaceTwo(char1,char2,s):
    return [c for c in s if c == char1 or c == char2]

unique = set(s)
m=0
for char in unique:
    for char2 in unique:
        s2 = replaceTwo(char,char2,s)
        if not consecCheck(s2):
            m = max(m,len(s2))       
print(m) 
