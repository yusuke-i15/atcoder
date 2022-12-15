mod = 998244353
N,M,K,S,T,X = map(int,input().split())
edge = [tuple(map(int,input().split())) for i in range(M)]
dp = [[[0]*(N+1) for i in range(K+1)] for j in range(2)]
dp[0][0][S] = 1
for i in range(K):
    for u,v in edge:
        for x in range(2):
            dp[x][i+1][v] += dp[x ^ (v==X)][i][u]
            dp[x][i+1][v] %= mod
            dp[x][i+1][u] += dp[x ^ (u==X)][i][v]
            dp[x][i+1][u] %= mod
print(dp[0][K][T])