N,K,D = map(int,input().split())
A = list(map(int,input().split()))
dp = [[[-1]*D for i in range(K+1)] for j in range(N+1)]
dp[0][0][0] = 0
for i in range(1,N+1):
    for j in range(K+1):
        for k in range(D):
            if dp[i-1][j][k] >= 0:
                dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k])
                if j+1 > K:
                    continue
                dp[i][j+1][(k+A[i-1])%D] = max(dp[i][j+1][(k+A[i-1])%D],dp[i-1][j][k]+A[i-1])
print(dp[N][K][0])