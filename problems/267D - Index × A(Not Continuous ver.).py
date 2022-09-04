N,M = map(int,input().split())
A = list(map(int,input().split()))

dp = [[0]*(M+1) for i in range(N+1)]
dp[0][0] = 0
dp[0][1] = -float("inf")
for i in range(1,N+1):
    for j in range(M+1):
        if j>i:
            dp[i][j] = -float("inf")
        elif j == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+A[i-1]*j)

print(dp[N][M])