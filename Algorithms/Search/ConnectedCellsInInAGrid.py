# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
n = int(input())
m = int(input())

mat = []
# get inputs
for _ in range(n):
    row = [int(i) for i in input().split()]
    mat.append(row)
    
def fill(i,j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    if mat[i][j] == 0 or mat[i][j] == '*':
        return 0
    mat[i][j] = '*' # mark it as visited
    return 1 + fill(i,j+1) + fill(i,j-1) + fill(i-1,j) + fill(i+1,j) + fill(i-1,j-1) + fill(i+1,j+1) + fill(i-1,j+1) + fill(i+1,j-1)

long = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] != 0:
            long = max(long, fill(i,j))
print(long)
