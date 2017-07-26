https://www.hackerrank.com/challenges/the-power-sum/

x = int(input())
n = int(input())
root = int(x ** (1.0/n))   # nth root of x

def power(j, total, count=0):
    total += (j ** n)
    if total == x: return count + 1
    if total > x: return 0
    
    # if total is not found, check all possible combinations from current counter till root.
    for i in range(j+1, root+1, 1):
        count = max(count, power(i,total, count))  # max: keep current count if recusurive calls return a lower value
    return count

print(power(0,0))
