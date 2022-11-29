mod = 998244353
N,M,K = map(int,input().split())
if K == 0:
    print(pow(M,N,mod))
else:
    dp = [[0]*M for i in range(N)]
    for i in range(M):
        dp[0][i] = 1
    for i in range(N-1):
        tmp = [0]
        for j in range(M):
            tmp.append(tmp[-1] + dp[i][j])
            tmp[-1] %= mod
        for j in range(M):
            dp[i+1][j] = tmp[max(j-K+1,0)] + tmp[M] - tmp[min(j+K,M)]
            dp[i+1][j] %= mod
    print(sum(dp[N-1])%mod)
