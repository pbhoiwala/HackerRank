# https://www.hackerrank.com/challenges/pairs/problem

def pairs(a,k):
    # a is the list of numbers and k is the difference value
    answer = 0
    setA = set(a)
    for num in a:
        if num + k in setA:
            answer += 1
    return answer
