import itertools
from itertools import combinations

N,M = map(int,input().split())

A = [[0] for i in range(M)]
for i in range(M):
    temp = list(map(int,input().split()))
    A[i] = temp[1:] 
comb = combinations(range(1,N+1),2)

ans = True
for i1,i2 in comb:
    flag = False
    for i in range(M):
        if i1 in A[i] and i2 in A[i]:
            flag = True
    if flag == False:
        ans = False
print("Yes" if ans else "No")