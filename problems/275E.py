N,M,K = map(int,input().split())
mod = 998244353
dp = [[0]*(N+1) for i in range(K+1)]
dp[0][0] = 1
for i in range(1,K+1):
    for j in range(1,M+1):
        for k in range(N+1):
            if k == N:
                dp[i][k] += dp[i-1][k]
            elif dp[i-1][k] != 0:
                if k + j <= N:
                    dp[i][k+j] += dp[i-1][k]
                else:
                    dp[i][j-k+N] += dp[i-1][k]
print(dp[K][N]%mod)

print(dp)