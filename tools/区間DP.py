
n = int(input())
M = list(tuple(map(int,input().split())) for i in range(n))
inf = float("inf")
dp = [[inf]*n for i in range(n)]

for i in range(n):
    dp[i][i] = 0

for W in range(1,n):
    for l in range(n-W):
        for i in range(l,l+W):
            dp[l][l+W] = min(dp[l][l+W],dp[l][i]+M[l][0]*M[i][1]*M[l+W][1]+dp[i+1][l+W]) 
print(dp[0][n-1])       
"""

N = int(input())
R = [0]*N
C = [0]*N
for i in range(N):
    R[i], C[i] = map(int, input().split())

INF = 10**18
dp = [[INF]*N for i in range(N)]
for i in range(N):
    dp[i][i] = 0
for l in range(1, N):
    for i in range(N-l):
        a0 = R[i]
        print(i,l,i+l)
        c0 = C[i+l]
        dp[i][i+l] = min(a0*C[j]*c0 + dp[i][j] + dp[j+1][i+l] for j in range(i, i+l))
print(dp[0][N-1])
print(dp)
"""