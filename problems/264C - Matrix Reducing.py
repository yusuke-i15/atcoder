import numpy as np
import itertools
 
h1,w1 = map(int,input().split())
A = [[0] for i in range(h1)]
for i in range(h1):
    A[i] = list(map(int,input().split()))
A = np.array(A)
 
h2,w2= map(int,input().split())
B = [[0] for i in range(h2)]
for i in range(h2):
    B[i] = list(map(int,input().split()))
B = np.array(B)
 
temp_h = itertools.combinations(range(h1), h2)
temp_w = itertools.combinations(range(w1), w2)
flag = False
 
for i in temp_h:
    temp = A[i,:]
    temp_w = itertools.combinations(range(w1), w2)
    for j in temp_w:
        temp2 = temp[:,j]
        if np.all(temp2==B):
            flag = True
            
print("Yes" if flag else "No")