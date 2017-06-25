# https://www.hackerrank.com/challenges/candies
n = int(input())
ratings = [int(input()) for _ in range(n)]
numCandies = [1]*n

for i in range(1,n,1):
    if ratings[i] > ratings[i-1]:
        numCandies[i] += numCandies[i-1]
for j in range(n-2,-1,-1):
    if ratings[j] > ratings[j+1] and numCandies[j] <= numCandies[j+1]:
        numCandies[j] = numCandies[j+1] + 1
print(sum(numCandies)) 
