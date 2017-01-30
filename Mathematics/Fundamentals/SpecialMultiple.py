# https://www.hackerrank.com/challenges/special-multiple
T = int(input());
for i in range(T):
    N = int(input())
    i = 1
    while(True):
        binI = str(bin(i)[2:]).replace('1','9')   # create a binary num and replace 1s with 9s
        if(int(binI) % N == 0):
            print(binI)
            break
        i+=1
