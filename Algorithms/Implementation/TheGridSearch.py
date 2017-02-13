def find_all(main_str, sub_str):
    begin = 0
    while True:
        begin = main_str.find(sub_str, begin)
        if begin == -1: return
        yield begin
        begin += 1

# populate 2D matrices G (grid) and P (pattern)
t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)

    i = 0               # counter for each row of the G
    pRows = len(P)      # number of rows in P
    pCols = len(P[0])   # number of columns in P
    found = False       # pattern found or not

    # Loop until the end of matrix is reached or Pattern is found
    while i < len(G) and not found:
        indices = list(find_all(G[i], P[0]))  # get indices of all occurrences of P[0] in the i'th row of G
        for k in indices:                     # loop through each individual index in indices
            newG = G[:]                       # copy G, just to be safe, not actually necessary
            r=(i,i+pRows)                     # indices for rows to slice from G
            s=(k,k+pCols)                     # indices for cols to slice from G
            # below one-liner slices G and extracts a sub-matrix that is same size of P
            sub = [newG[i][s[0]:s[1]] for i in range(len(newG))][r[0]:r[1]]
            if sub == P:                      # if extracted sub-matrix is same as P, then P is found, break loop
                found = True
                break
        i+=1                                  # else, check for next row in G
    print('YES' if found else 'NO')


'''
Since the code above may not be easy to understand, here is the logic that I've implemented.
So, there are two matrices, G and P.
Let's say G is
123412
561212
123634
781288

and P is
12
34

I iterate through evey single row in G and find indices where P[0] (which is '12') exists.
Then I go to those indices, and extract a matrix that is the same dimension of P.
So in first case, it extract ['12','56']. Then I simply check if this equals P or no. It would keep doing this
until ['12','34'] is found or end of G is reached.
'''