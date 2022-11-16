H,N = map(int,input().split())
dp = [[float("inf")]*(H+1) for i in range(N+1)]
dp[0][H] = 0
for i in range(1,N+1):
    a,b = map(int,input().split())
    for j in range(H,-1,-1):
        if dp[i-1][j] != float("inf"):
            dp[i][j] = dp[i-1][j]
    for j in range(H,-1,-1):
        if dp[i][j] != float("inf"):
            dp[i][max(0,j-a)] = min(dp[i][j]+b,dp[i][max(0,j-a)])
print(dp[N][0])