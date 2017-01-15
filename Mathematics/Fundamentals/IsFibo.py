# https://www.hackerrank.com/challenges/is-fibo
fibArr = [0,1]
for i in range(2,10000,1):
    fibArr.append(fibArr[i-1]+fibArr[i-2])

n = input()
for i in range(int(n)):
    x = input()
    if int(x) in fibArr:
        print("IsFibo")
    else:
        print("IsNotFibo")
