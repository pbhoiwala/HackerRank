# https://www.hackerrank.com/challenges/coin-change/
import sys

def getWays(amount, coins, coinIndex):
    # base cases return 1 if amount is made, otherwise 0 if all coins checked
    if amount == 0: return 1
    if coinIndex >= len(coins): return 0
    
    # make the key for cache hashmap with key = amount for coins[coinIndex] 
    # and value = numways that can happen. Then check if it exists in cache hashmap
    amtWithCoins = str(amount) + '+' + str(coinIndex)
    if amtWithCoins in cacheWays: 
        return cacheWays[amtWithCoins]
    
    ways, coinAmount = 0, 0
    # iterate until all coins are checked to make the amount
    # resursively iterate over amount that remains when each coin type is not used.
    while coinAmount <= amount:
        remaining = amount - coinAmount
        ways += getWays(remaining, coins, coinIndex+1)
        coinAmount += coins[coinIndex]
    cacheWays[amtWithCoins] = ways # cache the number of ways that amount 'x' with 'c' coins can be made
    return ways
 
# get inputs
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
cacheWays = {}
print(getWays(n, c, 0))
