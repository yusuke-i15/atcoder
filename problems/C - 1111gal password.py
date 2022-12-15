N = int(input())
dp = [[0]*(11) for i in range(N)]
mod = 998244353
for i in range(1,10):
    dp[0][i] = 1
for i in range(1,N):
    for j in range(1,10):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        dp[i][j] %= mod
print(sum(dp[N-1])%mod)