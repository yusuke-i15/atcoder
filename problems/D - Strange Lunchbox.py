N = int(input())
X,Y = map(int,input().split())
dp = [[[400]*(301) for i in range(301)] for i in range(N+1)]
dp[0][0][0] = 0
for i in range(1,N+1):
    A,B = map(int,input().split())
    for j in range(301):
        for k in range(301):
            dp[i][j][k] = min(dp[i-1][j][k],dp[i-1][max(0,j-A)][max(0,k-B)]+1)
if dp[N][X][Y] == 400:
    print(-1)
else:
    print(dp[N][X][Y])