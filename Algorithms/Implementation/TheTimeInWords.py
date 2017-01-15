# https://www.hackerrank.com/challenges/the-time-in-words
#!/bin/python3
import sys

sTime = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
         '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten',
         '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen',
         '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen',
         '19':'nineteen', '20':'twenty'}

def getStrTime(m):
    if m>30: m = 60-m
    if str(m) in sTime: return sTime[str(m)] + " minutes"
    else: return "twenty " + sTime[str(m)[1]] + " minutes"

def main(h,m):
    if m == 0: 
        time = "o' clock"
        return (sTime[str(h)] + " " + time)
    elif m == 15 or m == 45: time = "quarter"
    elif m == 30: time = "half"
    else: time = getStrTime(m)
    verb = ""
    if m > 30:
        verb = "to"
        h += 1
    else: verb = "past"  
    return (time + " " + verb + " " + sTime[str(h)])
    
h = int(input().strip())
m = int(input().strip())
print(main(h,m))
