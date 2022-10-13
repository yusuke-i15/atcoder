N,W = map(int,input().split())
dp = [[0]*(W+1) for i in range(N+1)]
for i in range(1,N+1):
    v,w = map(int,input().split())
    for j in range(1,W+1):
        if j-w >= 0:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v,dp[i][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][W])