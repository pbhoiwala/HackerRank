# https://www.hackerrank.com/challenges/almost-sorted/problem

n = int(input())
# get array inputs, add boundry pillars -1 and 1000001
d = [-1] + [int(i) for i in input().split()] + [1000001]

# special case if n is 2
if n == 2:
    if d[2] < d[1]: print("yes\nswap 1 2")
    exit()

# start/end store first/last elements of sub-array that is not sorted
start, end = [], []
# prev stores condition of i-1, so prev is True if d[i - 1] < d[i] < d[i + 1]
prev = True

# iterate over d and find out start/end values
for i in range(1, len(d) - 1, 1):
    if d[i - 1] < d[i] < d[i + 1]:
        if start and not prev:
            end = [d[i - 1], i - 1]
    elif not (d[i - 1] < d[i] < d[i + 1]) and (not start):
        start = [d[i], i]
    prev = d[i - 1] < d[i] < d[i + 1]

# If start/end values do not exist or if the values before and after start/end values
# are our of order. Otherwise, check if start/end values need to be swapped or reversed
if not start or not end:
    print("no")
elif (d[start[1] - 1] > d[end[1]]) or (d[end[1] + 1] < d[start[1]]) or (d[start[1]] < d[end[1] - 1]):
    print("no")
elif abs(end[1] - start[1]) == 1:
    print("yes\nswap", start[1], end[1])
elif d[start[1] + 1] < d[end[1] - 1] :
    print("yes\nswap", start[1], end[1])
elif d[start[1] + 1] > d[end[1] - 1]:
    print("yes\nreverse", start[1], end[1])
else:
    print("no")
