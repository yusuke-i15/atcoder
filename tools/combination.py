from itertools import combinations

N,M = map(int,input().split())
comb = combinations(range(M),2)
result = 0
A = [[0]*M for i in range(N)]
for i in range(N):
    A[i] = list(map(int,input().split()))
    
for i in comb:
    point = 0
    for j in range(N):
        point += max(A[j][i[0]],A[j][i[1]])
    result = max(result,point)
print(result)