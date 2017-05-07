# https://www.hackerrank.com/challenges/fibonacci-modified/submissions/code/43719878

t1,t2,n = input().split(' ')
#t1,t2,n = int(t1),int(t2),int(n)
t = [int(t1),int(t2)]

for i in range(2,int(n),1):
    tn = t[i-2] + (t[i-1]*t[i-1])
    t.append(tn)
    #print(t)
print(t[-1])
