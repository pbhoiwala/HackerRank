# https://www.hackerrank.com/challenges/diwali-lights
T = int(input())
for _ in range(T):
    b = int(input())
    print((2 ** b - 1) % 10 ** 5)
