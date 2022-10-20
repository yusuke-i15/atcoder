import numpy as np
N,K,Q = map(int,input().split())
P = [0]*N
for i in range(Q):
    A = int(input())
    P[A-1] += 1
P = np.array(P)
P = P - Q + K
ans = np.where(P>0,1,0)
for i in ans:
    print("Yes" if i else "No")